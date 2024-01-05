# SO fresh SO clean
The website is a simple shopping website where you can add the latest drip to 
your cart. When you start interacting with the website you notice that you can
add each of the items to your cart. When doing so you see a simple request
where the body contains XML used for selecting the item. 

Immediately you might try to select the flag item but you will be prompted with
an error message stating that it is an _Invalid item!_.

## Solution
When looking at the code we can see that the backend is rather simple:
```JavaScript
const express = require('express');
const path = require('node:path');
const bodyParser = require('body-parser');
const { readFile } = require('fs/promises');
const parseString = require('xml2js').parseString;

const app = express()
const port = 5000

app.use(express.static('static'))
app.use(bodyParser.text({ type: 'text/xml' }))

function invalidItem(item) {
    return JSON.stringify(item).includes('flag');
}

app.get('/', (req, res) => {
    res.sendFile('index.html', { root: path.join(__dirname, 'templates')});
})

app.get('/cart', async (req, res) => {
    let cartTemplate = await readFile('templates/cart.html', 'utf8');
    let html = cartTemplate.replaceAll('{{ item }}', 'Your cart is empty');
    res.setHeader('Content-Type', 'text/html');
    res.send(html);
})

app.post('/cart', async (req, res) => {
    let cart = null;
    let html = null;
    let cartTemplate = await readFile('templates/cart.html', 'utf8');
    try {
        parseString(req.body, function (err, cart) {
            if (invalidItem(cart)) {
                res.statusCode = 400;
                return res.send('Invalid item!');
            }
            if (cart.item.includes('flag')) {
                html = cartTemplate.replaceAll('{{ item }}', process.env.FLAG || 'gg{not_a_flag}');
            } else {
                html = cartTemplate.replaceAll('{{ item }}', cart.item)
            }
            res.setHeader('Content-Type', 'text/html');
            res.send(html);
        });
    } catch(e) {
        res.statusCode = 500;
        return res.send(e.message);
    }
})  

app.listen(port, () => {
    console.log(`listening on port ${port}`);
})
```

Most of the code is just boilerplate, it can be seen that the main logic is in 
the method handling `POST /cart`:

```JavaScript
app.post('/cart', async (req, res) => {
    let cart = null;
    let html = null;
    let cartTemplate = await readFile('templates/cart.html', 'utf8');
    try {
        parseString(req.body, function (err, cart) {
            if (invalidItem(cart)) {
                res.statusCode = 400;
                return res.send('Invalid item!');
            }
            if (cart.item.includes('flag')) {
                html = cartTemplate.replaceAll('{{ item }}', process.env.FLAG || 'gg{not_a_flag}');
            } else {
                html = cartTemplate.replaceAll('{{ item }}', cart.item)
            }
            res.setHeader('Content-Type', 'text/html');
            res.send(html);
        });
    } catch(e) {
        res.statusCode = 500;
        return res.send(e.message);
    }
})  
```

At this point it is clear that the objective of the challenge is to fetch the 
_flag_ item. That is we must make sure the cart includes a _flag_ item. However
to get to that point we must first bypass the `invalidItem` function.


```JavaScript
function invalidItem(item) {
    return JSON.stringify(item).includes('flag');
}
```

So we can see that `JSON.stringify(item).includes('flag')` must be false and 
that `cart.item.includes('flag')` has to be true for us to be able to get the
flag. Looking at this now, it seems rather weird, we `POST` a body containing XML
but the backend interacts with it as if it were JSON.

Looking closer, we can see that the `parseString` function is being called with
`req.body` as an argument. The `parseString` function is being imported from a 
library named `xml2js`. When reading up on `xml2js` we can see that it is a 
rather popular library used for parsing XML into a JavaScript object, with just
over 18 million downloads weekly.

Now for some this might ring warning beels immediately, that is cloning an XML
object into JSON. The thought that should popup is:

> Is this vulnerable to _prototype pollution_?

And the answer is _almost_, the library is actually vulnerable to _prototype 
poisoning_ a close relative to _prototype pollution_. This is well documented
in this [issue](https://github.com/Leonidas-from-XIV/node-xml2js/issues/593).

After reading up on prototype pollution and poisoning you might first try 
posting the following: `<__proto__><item>flag</item></__proto__>` and this is 
the correct solution.

Now why does this work? Look at how this differs from `<item>flag</item>`:
```
<item>flag</item>
JSON.stringify(item) --> {"item": "flag"}
cart.item --> "flag"

JSON.stringify(item).includes('flag') --> true
cart.item.includes('flag') --> true

<__proto__><item>flag</item></__proto__>
JSON.stringify(item) --> {}
cart.item --> ["flag"]

JSON.stringify(item).includes('flag') --> false
cart.item.includes('flag') --> true
```

The reason that `JSON.stringify(item)` returns an empty JSON object even though
`cart.item` outputs a value is because the prototype of the object has been 
poisoned. So the actual object does not include the _flag_ item but its 
prototype does and when calling `cart.item` JavaScript won't find the item on
the object itself so it looks into its prototype next, where it finds the item.

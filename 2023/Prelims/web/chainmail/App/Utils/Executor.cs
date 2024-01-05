namespace App.Utils;

using System.Diagnostics;
using System.Net.Http;

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

class RunResult {
    public bool Success { get; set; }
    public string? Output { get; set; }
}
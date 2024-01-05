using System.Diagnostics;

static class CommandRunner
{
    public static int RunCommand(this string cmd, string args) 
    { 
        using (Process process = new Process())
        {
            process.StartInfo.UseShellExecute = true;
            process.StartInfo.FileName = cmd;
            process.StartInfo.Arguments = args;
            process.StartInfo.CreateNoWindow = true;
            process.Start();
            process.WaitForExit();
            return process.ExitCode;
        }
    } 
}
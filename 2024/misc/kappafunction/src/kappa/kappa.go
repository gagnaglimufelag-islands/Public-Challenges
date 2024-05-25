package kappa

import (
	"os"

	"github.com/dop251/goja"
	"github.com/dop251/goja_nodejs/console"
	"github.com/dop251/goja_nodejs/require"
)

type Kappa struct {
}

type ScriptOutput struct {
	ReturnValue string
	Stdout      string
	Stderr      string
}

func (k Kappa) Do(script string) (ScriptOutput, error) {

	var stdoutStr, stderrStr string

	printer := console.StdPrinter{
		StdoutPrint: func(s string) { stdoutStr += s },
		StderrPrint: func(s string) { stderrStr += s },
	}

	registry := new(require.Registry)
	runtime := goja.New()

	registry.Enable(runtime)
	registry.RegisterNativeModule("console", console.RequireWithPrinter(printer))

	runtime.RunScript("kappafunction", "var this_is_what_you_are_looking_for='"+os.Getenv("FLAG")+"'")

	val, err := runtime.RunScript("kappafunction", script)

	if err, ok := err.(*goja.Exception); ok {
		return ScriptOutput{
			ReturnValue: "Error in script",
			Stdout:      stdoutStr,
			Stderr:      stderrStr,
		}, err
	}

	return ScriptOutput{
		ReturnValue: val.ToString().String(),
		Stdout:      stdoutStr,
		Stderr:      stderrStr,
	}, nil
}

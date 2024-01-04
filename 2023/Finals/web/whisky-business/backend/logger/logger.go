package logger

import (
	"os"

	"github.com/sirupsen/logrus"
)

var Log *logrus.Logger // share with all packages

func init() {
	Log = logrus.New()
	// Log as JSON instead of the default ASCII formatter.
	Log.SetFormatter(&logrus.TextFormatter{})
	/*if Environment == "PROD" {
		Log.SetFormatter(&logrus.JSONFormatter{})
	} else {
		// The TextFormatter is default, you don't actually have to do this.
		Log.SetFormatter(&logrus.TextFormatter{})
	}*/

	// Output to stdout instead of the default stderr
	// Can be any io.Writer, see below for File example
	Log.SetOutput(os.Stdout)

	// Only log the warning severity or above.
	Log.SetLevel(logrus.InfoLevel)
}

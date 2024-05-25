package main

import (
	"net/http"
	"os"

	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/cookie"
	"github.com/gin-gonic/gin"

	// Super proprietary code in here
	"ggfi/kappafunctions/kappa"
)

type ScriptForm struct {
	Content string `form:"content" binding:"required"`
}

func main() {
	router := gin.Default()

	store := cookie.NewStore([]byte(os.Getenv("cookie_secret")))
	router.Use(sessions.Sessions("kappa_session", store))

	router.GET("/", index)
	router.POST("/", do)

	router.LoadHTMLGlob("templates/*")

	router.Run()
}

func index(c *gin.Context) {
	session := sessions.Default(c)

	c.HTML(http.StatusOK,
		"index.html",
		gin.H{
			"session": session.Get("hello"),
		})
}

func do(c *gin.Context) {
	session := sessions.Default(c)
	var form ScriptForm
	err := c.ShouldBind(&form)

	if err != nil {
		c.HTML(http.StatusOK,
			"index.html",
			gin.H{
				"text": "Error", "output": kappa.ScriptOutput{ReturnValue: "", Stderr: err.Error(), Stdout: ""}, "session": session.Get("hello"),
			})
		return
	}

	var k kappa.Kappa
	output, err := k.Do(form.Content)

	if err != nil {
		c.HTML(http.StatusOK,
			"index.html",
			gin.H{
				"text": "Error", "output": kappa.ScriptOutput{ReturnValue: "", Stderr: err.Error(), Stdout: ""}, "session": session.Get("hello"),
			})
		return
	}

	c.HTML(http.StatusOK,
		"index.html",
		gin.H{
			"text": "SUCCESS", "output": output, "session": session.Get("hello"),
		})
}

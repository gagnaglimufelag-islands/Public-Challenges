package app

import (
  "os"
	"log"

	"timeclock/controllers"
	"timeclock/middlewares"
	"timeclock/models"

	"github.com/gorilla/mux"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type App struct {
	Router *mux.Router
	DB     *gorm.DB
}

func (a *App) Connect(connectionString string) {
	var err error
	a.DB, err = gorm.Open(mysql.Open(connectionString), &gorm.Config{})
	if err != nil {
		log.Fatal(err)
		panic("Cannot connect to DB")
	}
	log.Println("Connected to Database...")
}

func (a *App) Migrate() {
	if err := a.DB.AutoMigrate(
		&models.User{},
		&models.TimeRegister{},
		&models.Project{},
		&models.Inventory{},
		&models.GlassBox{},
		&models.BluePrint{},
		&models.Measurement{}); err != nil {
		log.Fatal(err)
		panic("Database migration failed")
	}
  
  admin := &models.User{Name: "Admin Johnson", Username: "Administrator", Email: "admin@admin.god", Password: os.Getenv("FLAG"), Administrator: true}
  a.DB.Create(&admin)

	log.Println("Database Migration Completed...")
}

func (a *App) InitializeRoutes() {
	a.Router.Handle("/token", controllers.GenerateToken(a.DB)).Methods("POST")

	a.Router.Handle("/user", controllers.GetUsers(a.DB)).Methods("GET") // check token if user has sufficient privledges to execute this operation
	a.Router.Handle("/user/{id}", controllers.GetUser(a.DB)).Methods("GET")
	a.Router.Handle("/user/register", controllers.CreateUser(a.DB)).Methods("POST")
	// a.Router.Handle("/user/{id}", controllers.UpdateUser(a.DB)).Methods("PUT")
	// a.Router.Handle("/user/{id}", controllers.DeleteUser(a.DB)).Methods("DELETE")

	a.Router.Handle("/project", controllers.GetProjects(a.DB)).Methods("GET")
	a.Router.Handle("/project/{id}", controllers.GetProject(a.DB)).Methods("GET")

	a.Router.Handle("/project/", controllers.CreateProject(a.DB)).Methods("POST")
	a.Router.Handle("/project/{id}", controllers.UpdateProject(a.DB)).Methods("PUT")
	a.Router.Handle("/project/{id}", controllers.DeleteProject(a.DB)).Methods("DELETE")

	a.Router.Handle("/timeregistration/clockin", controllers.TimeRegistrationClockIn(a.DB)).Methods("POST")
	a.Router.Handle("/timeregistration/clockout", controllers.TimeRegistrationClockOut(a.DB)).Methods("POST")
	a.Router.Handle("/timeregistration/status", controllers.TimeRegistrationStatus(a.DB)).Methods("GET")

	//
	a.Router.Handle("/inventory/glassbox/{boxid}/{internalname}", controllers.InventoryCreateGlassBox(a.DB)).Methods("POST")
	a.Router.Handle("/inventory/glassbox/{nameorid}", controllers.InventoryGetGlassBox(a.DB)).Methods("GET")
	a.Router.Handle("/inventory/glassbox", controllers.InventoryGetGlassBox(a.DB)).Methods("GET")
	a.Router.Handle("/inventory/glassbox/{nameorid}", controllers.InventoryUpdateGlassBox(a.DB)).Methods("PUT")
	a.Router.Handle("/inventory/glassbox/{nameorid}", controllers.InventoryDeleteGlassBox(a.DB)).Methods("DELETE")

	a.Router.Handle("/inventory/blueprint", controllers.InventoryCreateBluePrint(a.DB)).Methods("POST")
	a.Router.Handle("/inventory/blueprint/{name}", controllers.InventoryGetBluePrint(a.DB)).Methods("GET")
	a.Router.Handle("/inventory/blueprint", controllers.InventoryGetBluePrint(a.DB)).Methods("GET")
	a.Router.Handle("/inventory/blueprint/{name}", controllers.InventoryUpdateBluePrint(a.DB)).Methods("PUT")
	a.Router.Handle("/inventory/blueprint/{name}", controllers.InventoryDeleteBluePrint(a.DB)).Methods("DELETE")

	// search func. to compare buleprints against glass boxes.
	a.Router.Handle("/inventory/compare", controllers.InventoryCompareBluePrintAndGlassBox(a.DB)).Methods("GET")

	a.Router.Use(middlewares.Auth)
}

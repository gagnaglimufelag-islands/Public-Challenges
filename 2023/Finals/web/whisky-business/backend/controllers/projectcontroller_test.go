package controllers

import (
   "fmt"
   "database/sql/driver"
   "net/http"
   "net/http/httptest"
   //"regexp"
   "testing"
   "time"

   "github.com/gorilla/mux"
   "gorm.io/driver/mysql"
   "gorm.io/gorm"
   "github.com/DATA-DOG/go-sqlmock"
   "github.com/steinfletcher/apitest"
   jsonpath "github.com/steinfletcher/apitest-jsonpath"

   //"github.com/gookit/goutil/dump"
)


// Argument interface allows to match
// any argument in specific way when used with
// ExpectedQuery and ExpectedExec expectations.
type Argument interface {
   Match(driver.Value) bool
}

// AnyArg will return an Argument which can
// match any kind of arguments.
//
// Useful for time.Time or similar kinds of arguments.
func AnyArg() Argument {
   return anyArgument{}
}

type anyArgument struct{}

func (a anyArgument) Match(_ driver.Value) bool {
   return true
}

// Result satisfies sql driver Result, which
// holds last insert id and rows affected
// by Exec queries
type result struct {
   insertID     int64
   rowsAffected int64
   err          error
}

// NewResult creates a new sql driver Result
// for Exec based query mocks.
func NewResult(lastInsertID int64, rowsAffected int64) driver.Result {
   return &result{
      insertID:     lastInsertID,
      rowsAffected: rowsAffected,
   }
}

func (r *result) LastInsertId() (int64, error) {
   return r.insertID, r.err
}

func (r *result) RowsAffected() (int64, error) {
   return r.rowsAffected, r.err
}

type NullTime struct {
   Time  time.Time
   Valid bool // Valid is true if Time is not NULL
}

type AnyTime struct{}

func (a AnyTime) Match(v driver.Value) bool {
   _, ok := v.(time.Time)
   return ok
}

func Test_GetProject(t *testing.T) {
   db, mock, err := sqlmock.New()
   if err != nil {
      t.Fatalf("an error '%s' was not expected when opening a stub database connection", err)
   }
   defer db.Close()

   gormDB, err := gorm.Open(mysql.New(mysql.Config{
      Conn: db,
      SkipInitializeWithVersion: true,
   }), &gorm.Config{})
   if err != nil {
      panic(err) // Error here
   }

   var (
      id            = uint(1)
      name          = "Valshlid"
      description   = "Rand byggður kassi við Hlidarenda i RVK"
   )

   mock.ExpectQuery("SELECT(.*)").
      WithArgs(id).
      WillReturnRows(sqlmock.NewRows([]string{"id", "name", "description"}).
      AddRow(id, name, description))

   r := mux.NewRouter()
   r.HandleFunc("/project/{id}", GetProject(gormDB)).Methods("GET")
   ts := httptest.NewServer(r)
   defer ts.Close()
   apitest.New().
      //Debug().
      Handler(r).
      Get("/project/1").
      Expect(t).
      Body(`{"CreatedAt":"0001-01-01T00:00:00Z","UpdatedAt":"0001-01-01T00:00:00Z","DeletedAt":null,"ID":1,"name":"Valshlid","description":"Rand byggður kassi við Hlidarenda i RVK"}`).
      Status(http.StatusOK).
      Assert(jsonpath.Equal(`$.ID`, float64(1))).
      End()
}

func Test_GetProjects(t *testing.T) {
   db, mock, err := sqlmock.New()
   if err != nil {
      t.Fatalf("an error '%s' was not expected when opening a stub database connection", err)
   }
   defer db.Close()

   gormDB, err := gorm.Open(mysql.New(mysql.Config{
      Conn: db,
      SkipInitializeWithVersion: true,
   }), &gorm.Config{})
   if err != nil {
      panic(err) // Error here
   }

   rows := sqlmock.NewRows([]string{"id", "name", "description"}).
      AddRow(uint(1), "name1", "description1").
      AddRow(uint(2), "name2", "description2").
      AddRow(uint(3), "name3", "description3")

   mock.ExpectQuery("SELECT").
      WillReturnRows(rows)

   r := mux.NewRouter()
   r.HandleFunc("/project", GetProjects(gormDB)).Methods("GET")
   ts := httptest.NewServer(r)
   defer ts.Close()
   apitest.New().
      //Debug().
      Handler(r).
      Get("/project").
      Expect(t).
      Status(http.StatusOK).
      Assert(jsonpath.Len("$", 3)).
      End()
}

func Test_CreateProject(t *testing.T) {
   db, mock, err := sqlmock.New()
   if err != nil {
      t.Fatalf("an error '%s' was not expected when opening a stub database connection", err)
   }
   defer db.Close()

   gormDB, err := gorm.Open(mysql.New(mysql.Config{
      Conn: db,
      SkipInitializeWithVersion: true,
   }), &gorm.Config{})
   if err != nil {
      panic(err) // Error here
   }

   var (
      userID             = uint(1)
      userName           = "Jon"
      userUsername       = "johnny"
      userEmail          = "email@email.com"
      userAdministrator  = true
   )

   mock.ExpectQuery("SELECT(.*)").
      WillReturnRows(sqlmock.NewRows([]string{"id", "name", "username", "email", "administrator"}).
      AddRow(userID, userName, userUsername, userEmail, userAdministrator))

   // insert
   //var deletedat NullTime
   //mock.MatchExpectationsInOrder(false)
   mock.ExpectBegin()
   mock.ExpectExec("^INSERT (.+)").
      //WithArgs(AnyArg(), AnyArg(), AnyArg(), "sdf", "sljd").
      WillReturnResult(&result{insertID:int64(1),rowsAffected:int64(1)})
   fmt.Println(mock.ExpectationsWereMet())
   mock.ExpectCommit()

   r := mux.NewRouter()
   r.HandleFunc("/project", CreateProject(gormDB)).Methods("POST")
   ts := httptest.NewServer(r)
   defer ts.Close()
   apitest.New().
      Debug().
      Handler(r).
      Post("/project").
      //Body(fmt.Sprintf(`{"name": "%s", "description": %s}`, name, description)).
      Expect(t).
      //Body(`{"CreatedAt":"0001-01-01T00:00:00Z","UpdatedAt":"0001-01-01T00:00:00Z","DeletedAt":null,"ID":1,"name":"Valshlid","description":"Rand byggður kassi við Hlidarenda i RVK"}`).
      Status(http.StatusOK).
      End()
}

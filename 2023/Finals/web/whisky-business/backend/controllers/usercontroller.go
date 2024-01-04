package controllers

import (
	"encoding/json"
	"net/http"
	"fmt"
	"strconv"

	"timeclock/error"
	"timeclock/auth"
	"timeclock/logger"
	"timeclock/models"
	"timeclock/utils"

	"github.com/gookit/goutil/dump"
	"github.com/gorilla/mux"
	"github.com/sirupsen/logrus"
	"gorm.io/gorm"
)

func GetUsers(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		tokenString := r.Header.Get("Authorization")
		u := &models.User{}
		u.Email, _ = auth.ValidateToken(tokenString)
		if errResp := u.GetUserByEmail(db); errResp != nil {
			logger.Log.Error(fmt.Sprintf("User with ID: %s not found!", strconv.FormatUint(uint64(u.ID), 10)))
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("User with ID: %s not found!", strconv.FormatUint(uint64(u.ID), 10)))))
			return
		}

		if !u.Administrator {
			logger.Log.Error(fmt.Sprintf("User %s does not have sufficient privledges to create a project!", u.Name))
			w.WriteHeader(http.StatusUnauthorized)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("User %s does not have sufficient privledges to list users!", u.Name))))
			return
		}

		user := &models.User{}
		users, err := user.GetUsers(db)
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(users)
	}
}

func GetUser(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		w.Header().Set("Access-Control-Allow-Origin", "*")

		tokenString := r.Header.Get("Authorization")
		u := &models.User{}
		u.Email, _ = auth.ValidateToken(tokenString)
		if errResp := u.GetUserByEmail(db); errResp != nil {
			logger.Log.Error(fmt.Sprintf("User with ID: %s not found!", strconv.FormatUint(uint64(u.ID), 10)))
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("User with ID: %s not found!", strconv.FormatUint(uint64(u.ID), 10)))))
			return
		}

		if !u.Administrator {
			logger.Log.Error(fmt.Sprintf("User %s does not have sufficient privledges to create a project!", u.Name))
			w.WriteHeader(http.StatusUnauthorized)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("User %s does not have sufficient privledges to list users!", u.Name))))
			return
		}

		userId, err := utils.CastStringToUint(mux.Vars(r))
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		user := &models.User{}
		user.ID = userId[0]
		if errResp := user.GetUser(db); errResp != nil {
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(user)
	}
}

func CreateUser(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		var user models.User

		if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		if err := user.HashPassword(user.Password); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		if err := user.CreateUser(db); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info(user)

		json.NewEncoder(w).Encode(user)
		w.WriteHeader(http.StatusOK)
	}
}

func UpdateUser(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		uintParams, err := utils.CastStringToUint(mux.Vars(r))
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		user := &models.User{}
		user.ID = uintParams[0]
		if err := user.GetUser(db); err != nil {
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		// drop user.Projects obj.
		user.Projects = nil
		if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		//dump.P(user)
		if errResp := user.UpdateUser(db); errResp != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(errResp)))
			return
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(user)
	}
}

func DeleteUser(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		uintParams, err := utils.CastStringToUint(mux.Vars(r))
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		user := &models.User{}
		user.ID = uintParams[0]
		if errResp := user.GetUser(db); errResp != nil {
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		dump.P(user)

		if errResp := user.DeleteUser(db); errResp != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(errResp)
			return
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(user)
	}
}

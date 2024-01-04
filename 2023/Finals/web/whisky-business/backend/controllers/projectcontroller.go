package controllers

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"timeclock/auth"
	"timeclock/error"
	"timeclock/logger"
	"timeclock/models"
	"timeclock/utils"

	//"github.com/gookit/goutil/dump"
	"github.com/gorilla/mux"
	"github.com/sirupsen/logrus"
	"gorm.io/gorm"
)

func GetProjects(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		w.Header().Set("Access-Control-Allow-Origin", "*")

		p := &models.Project{}
		projects, err := p.GetProject(db)
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusNotFound)
			if err := json.NewEncoder(w).Encode(err); err != nil {
				logger.Log.Error(err)
			}
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host":   r.URL.Host,
			"path":   r.URL.Path,
			"header": r.Header,
		}).Info()

		w.WriteHeader(http.StatusOK)
		if err := json.NewEncoder(w).Encode(projects); err != nil {
			logger.Log.Error(err)
		}
	}
}

func GetProject(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		uintParams, err := utils.CastStringToUint(mux.Vars(r))
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			if err := json.NewEncoder(w).Encode(err); err != nil {
				logger.Log.Error(err)
			}
			return
		}

		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			if err := json.NewEncoder(w).Encode(err); err != nil {
				logger.Log.Error(err)
			}
			return
		}

		p := &models.Project{}
		p.ID = uintParams[0]
		projects, errResp := p.GetProject(db)
		//dump.P(projects)
		if errResp != nil {
			w.WriteHeader(http.StatusNotFound)
			if err := json.NewEncoder(w).Encode(errResp); err != nil {
				logger.Log.Error(err)
			}
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host":   r.URL.Host,
			"path":   r.URL.Path,
			"header": r.Header,
		}).Info()

		w.WriteHeader(http.StatusOK)
		if err := json.NewEncoder(w).Encode(projects[0]); err != nil {
			logger.Log.Error(err)
		}
	}
}

// TODO: use as reference for logging!
func CreateProject(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		tokenString := r.Header.Get("Authorization")

		var p models.Project
		if err := json.NewDecoder(r.Body).Decode(&p); err != nil {
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

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
			json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("User %s does not have sufficient privledges to create a project!", u.Name))))
			return
		}

		if err := p.CreateProject(db); err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info(p)

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(p)
	}
}

func UpdateProject(db *gorm.DB) http.HandlerFunc {
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
			logger.Log.Error(fmt.Sprintf("User %s does not have sufficient privledges to delete a project!", u.Name))
			w.WriteHeader(http.StatusUnauthorized)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("User %s does not have sufficient privledges to delete a project!", u.Name))))
			return
		}

		uintParams, err := utils.CastStringToUint(mux.Vars(r))
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		var p models.Project
		if err := json.NewDecoder(r.Body).Decode(&p); err != nil {
			logger.Log.Error(err)
		}
		p.ID = uintParams[0]
		if err := p.UpdateProject(db); err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host":   r.URL.Host,
			"path":   r.URL.Path,
			"header": r.Header,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(p)
	}
}

func DeleteProject(db *gorm.DB) http.HandlerFunc {
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
			logger.Log.Error(fmt.Sprintf("User %s does not have sufficient privledges to delete a project!", u.Name))
			w.WriteHeader(http.StatusUnauthorized)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("User %s does not have sufficient privledges to delete a project!", u.Name))))
			return
		}

		uintParams, err := utils.CastStringToUint(mux.Vars(r))
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		p := &models.Project{}
		p.ID = uintParams[0]
		if err := p.DeleteProject(db); err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(p)
	}
}

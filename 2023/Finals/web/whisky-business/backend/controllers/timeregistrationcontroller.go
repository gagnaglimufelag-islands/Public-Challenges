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

	"github.com/gookit/goutil/dump"
	"gorm.io/gorm"
)

func TimeRegistrationClockIn(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		w.Header().Set("Access-Control-Allow-Origin", "*")

		// comment out for localhost testing and developing.
		tokenString := r.Header.Get("Authorization")
		fmt.Println("auth: ", tokenString)
		u := &models.User{}
		u.Email, _ = auth.ValidateToken(tokenString)
		if errResp := u.GetUserByEmail(db); errResp != nil {
			logger.Log.Error(fmt.Sprintf("User with ID: %s not found!", strconv.FormatUint(uint64(u.ID), 10)))
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("User with ID: %s not found!", strconv.FormatUint(uint64(u.ID), 10)))))
			return
		}

		var tr models.TimeRegister
		if err := json.NewDecoder(r.Body).Decode(&tr); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		tr.UserID = 2

		if err := tr.ClockIn(db); err != nil {
			dump.P(err)
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(err)
			return
		}

		w.WriteHeader(http.StatusOK)
	}
}

func TimeRegistrationClockOut(db *gorm.DB) http.HandlerFunc {
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

		var tr models.TimeRegister
		if err := json.NewDecoder(r.Body).Decode(&tr); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}
		tr.UserID = u.ID

		if errResp := tr.ClockOut(db); errResp != nil {
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(errResp)
			return
		}

		w.WriteHeader(http.StatusOK)
	}
}

// TimeRegistrationStatus to see if user is currently clocked-in or not.
func TimeRegistrationStatus(db *gorm.DB) http.HandlerFunc {
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

		var tr models.TimeRegister
		tr.UserID = u.ID

		isClockedIn, err := tr.ClockedInStatus(db)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		json.NewEncoder(w).Encode(isClockedIn)
		w.WriteHeader(http.StatusOK)
	}
}

package controllers

import (
	"encoding/json"
	"net/http"

	"timeclock/auth"
	"timeclock/error"
	"timeclock/logger"
	"timeclock/models"

	"github.com/sirupsen/logrus"
	"gorm.io/gorm"
)

type TokenRequest struct {
	Email    string `json:"email"`
	Password string `json:"password"`
}

type TokenResponse struct {
	Token string `json:"token"`
}

func GenerateToken(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		w.Header().Set("Access-Control-Allow-Origin", "*")
		
		var request TokenRequest
		var user models.User

		if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		// check if email exists and password is correct
		user.Email = request.Email
		if err := user.GetUserByEmail(db); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(err)
			return
		}
		if err := user.CheckPassword(request.Password); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusUnauthorized)
			json.NewEncoder(w).Encode(err)
			return
		}

		tokenString, err := auth.GenerateJWT(user.Email, user.Username)
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(err)
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host":   r.URL.Host,
			"path":   r.URL.Path,
			"header": r.Header,
			// as you can see, there is a lot the logger can do for us
			// however "body": r.Body will not work, and always log an empty string!
			//"body":     req
			// this is why we'll log our crated struct instead.
		}).Info(tokenString)

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(TokenResponse{Token: tokenString})
	}
}

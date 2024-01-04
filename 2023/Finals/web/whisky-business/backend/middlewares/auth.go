package middlewares

import (
	"encoding/json"
	"fmt"
	"net/http"

	"timeclock/auth"
	"timeclock/error"
	"timeclock/logger"
)

func Auth(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		tokenString := r.Header.Get("Authorization")
		if r.RequestURI != "/token" && r.RequestURI != "/user/register" {
			if tokenString == "" {
				logger.Log.Error("request does not contain an access token")
				w.WriteHeader(http.StatusUnauthorized)
				json.NewEncoder(w).Encode(error.New(error.WithDetails(fmt.Sprintf("{'error': 'request does not contain an access token'}"))))
				return
			}
			if _, err := auth.ValidateToken(tokenString); err != nil {
				logger.Log.Error(fmt.Sprintf("%v", err))
				w.WriteHeader(http.StatusUnauthorized)
				json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
				return
			}
		}
		next.ServeHTTP(w, r)
	})
}

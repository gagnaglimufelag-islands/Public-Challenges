package controllers

import (
	"encoding/json"
	"io"
	"net/http"
	"timeclock/error"
	"timeclock/logger"
	"timeclock/models"
	"timeclock/utils"

	"github.com/gorilla/mux"
	"github.com/sirupsen/logrus"
	"gorm.io/gorm"
)

func InventoryCreateGlassBox(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/(text|json); charset=UTF-8")

		vars := mux.Vars(r)
		boxID, err := utils.CastParamToUint(vars["boxid"])
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(err)
			return
		}

		glassBoxRawData, err := io.ReadAll(r.Body)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
		}

		glassBoxResponse, err := models.CreateGlassBox(db, boxID, vars["internalname"], glassBoxRawData)
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(err)
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(glassBoxResponse)
	}
}

func InventoryGetGlassBox(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		glassBox, err := models.GetGlassBox(db, mux.Vars(r)["nameorid"])
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info(glassBox)

		if len(glassBox) == 1 {
			w.WriteHeader(http.StatusOK)
			json.NewEncoder(w).Encode(glassBox[0])
		} else {
			w.WriteHeader(http.StatusOK)
			json.NewEncoder(w).Encode(glassBox)
		}
	}
}

func InventoryUpdateGlassBox(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		var gb models.GlassBox
		if err := json.NewDecoder(r.Body).Decode(&gb); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
		}

		if err := gb.UpdateGlassBox(db, mux.Vars(r)["nameorid"]); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(gb)
	}
}

func InventoryDeleteGlassBox(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		glassBox, err := models.DeleteGlassBox(db, mux.Vars(r)["nameorid"])
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(glassBox)
	}
}

func InventoryCreateBluePrint(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		var bp models.BluePrint
		if err := json.NewDecoder(r.Body).Decode(&bp); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
		}

		if err := bp.CreateBluePrint(db); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(err)
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(bp)
	}
}

func InventoryGetBluePrint(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		var bluePrints []models.BluePrint
		bluePrints, err := models.GetBluePrint(db, mux.Vars(r)["name"])
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(err)
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		if len(bluePrints) == 1 {
			w.WriteHeader(http.StatusOK)
			json.NewEncoder(w).Encode(bluePrints[0])
		} else {
			w.WriteHeader(http.StatusOK)
			json.NewEncoder(w).Encode(bluePrints)
		}

	}
}

func InventoryUpdateBluePrint(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		var bp models.BluePrint
		if err := json.NewDecoder(r.Body).Decode(&bp); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
		}

		if err := bp.UpdateBluePrint(db, mux.Vars(r)["name"]); err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(bp)
	}
}

func InventoryDeleteBluePrint(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		bp, err := models.DeleteBluePrint(db, mux.Vars(r)["name"])
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(error.New(error.WithDetails(err)))
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(bp)
	}
}

func InventoryCompareBluePrintAndGlassBox(db *gorm.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")

		results, err := models.CompareBluePrintWithGlassBox(db, r.URL.Query())
		if err != nil {
			logger.Log.Error(err)
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(err)
			return
		}

		logger.Log.WithFields(logrus.Fields{
			"host": r.URL.Host,
			"path": r.URL.Path,
		}).Info()

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(results)
	}
}

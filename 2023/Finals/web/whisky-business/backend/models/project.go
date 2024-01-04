package models

import (
	"fmt"
	"strconv"

	"timeclock/logger"

	"gorm.io/gorm"
)

type Project struct {
	gorm.Model
	Name        string `json:"name" gorm:"unique"`
	Description string `json:"description"`
}

// GetProject returns idividual record if project.id is attached to the project object
// otherwise returns all project records.
func (project *Project) GetProject(db *gorm.DB) ([]Project, error) {
	var projects []Project

	if project.ID != 0 {
		if err := db.First(&projects, project.ID).Error; err != nil {
			return nil, err
		}
	} else {
		if err := db.Find(&projects).Error; err != nil {
			return nil, err
		}
	}

	return projects, nil
}

func (project *Project) CreateProject(db *gorm.DB) error {
	if err := db.Create(&project).Error; err != nil {
		return err
	}

	return nil
}

// TODO: look into some validation before and after db action.
func (project *Project) UpdateProject(db *gorm.DB) error {
	result := db.Model(&project).Updates(Project{Name: project.Name, Description: project.Description})
	if result.Error != nil {
		return result.Error
	}
	if result.RowsAffected < 1 {
		customError := fmt.Sprintf("Can't update project with id: %s it does not exists!", strconv.FormatUint(uint64(project.ID), 10))
		logger.Log.Error(customError)
		return fmt.Errorf(customError)
	}

	return nil
}

// TODO: implement logging and returning to user error handling as is done here.
func (project *Project) DeleteProject(db *gorm.DB) error {
	result := db.Delete(&project)
	if result.Error != nil {
		return result.Error
	}
	if result.RowsAffected < 1 {
		customError := fmt.Sprintf("Can't delete project with id: %s it does not exists!", strconv.FormatUint(uint64(project.ID), 10))
		logger.Log.Error(customError)
		return fmt.Errorf(customError)
	}

	return nil
}

package models

import (
	"bufio"
	"bytes"
	"errors"
	"fmt"
	"net/url"
	"strconv"
	"strings"

	"github.com/gookit/goutil/dump"
	"gorm.io/gorm"
)

type Inventory struct {
	gorm.Model
	Type string
}

type BluePrint struct {
	ID           uint   `gorm:"primaryKey"`
	Name         string `gorm:"unique;size:191"`
	Measurements []Measurement
}

type GlassBox struct {
	BoxID        uint          `gorm:"primaryKey;autoIncrement:false"`
	InternalName string        `gorm:"unique;size:191"`
	Measurements []Measurement `gorm:"foreignKey:GlassBoxID"`
}

type Measurement struct {
	ID          uint `gorm:"primaryKey"`
	Width       int  `json:"width" gorm:"not null"`
	Height      int
	Thickness   int
	Quantity    int
	GlassBoxID  *uint
	BluePrintID *uint
}

type Result struct {
	BoxID        int
	Name         string
	InternalName string
	Width        int `json:"width" gorm:"not null"`
	Height       int
	Thickness    int
	Quantity     int
}

func CreateGlassBox(db *gorm.DB, boxID uint, internalName string, glassBoxData []byte) (*GlassBox, error) {
	count := make(map[Measurement]int)
	var measurements []Measurement
	scanner := bufio.NewScanner(bytes.NewReader(glassBoxData))
	for scanner.Scan() {
		m, err := parseMeasurement(scanner.Text())
		if err != nil {
			continue
		}
		m.GlassBoxID = &boxID

		if n := count[m]; n > 0 {
			count[m] = n + 1
		} else {
			count[m] = 1
			measurements = append(measurements, m)
		}
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}

	for i := range measurements {
		(&measurements[i]).Quantity = count[measurements[i]]
	}

	glassBox := GlassBox{BoxID: boxID, InternalName: internalName}
	transactionError := db.Transaction(func(tx *gorm.DB) error {
		// create first all glasses in glass_boxes table
		// followed by inserting into measurements table.
		if err := tx.Create(&glassBox).Error; err != nil {
			return err
		}
		if err := tx.Create(&measurements).Error; err != nil {
			return err
		}

		return nil
	})
	if transactionError != nil {
		return nil, transactionError
	}

	return &GlassBox{
		BoxID:        boxID,
		InternalName: internalName,
		Measurements: measurements,
	}, nil
}

// GetGlassBox handles both get a GlassBox and get all GlassBoxes.
func GetGlassBox(db *gorm.DB, glassBoxNameOrID string) ([]GlassBox, error) {
	var glassBoxes []GlassBox
	var err error

	if glassBoxNameOrID != "" {
		if err = db.Preload("Measurements").First(&glassBoxes, "internal_name = ?", glassBoxNameOrID).Error; err != nil {
			if errors.Is(err, gorm.ErrRecordNotFound) {
				if err = db.Preload("Measurements").First(&glassBoxes, "box_id = ?", glassBoxNameOrID).Error; err != nil {
					return nil, err
				}
			}
		}
	} else {
		err = db.Preload("Measurements").Find(&glassBoxes).Error
	}
	if err != nil {
		return nil, err
	}

	return glassBoxes, nil
}

func (glassBox *GlassBox) UpdateGlassBox(db *gorm.DB, glassBoxNameOrID string) error {
	getGlassBox, err := GetGlassBox(db, glassBoxNameOrID)
	if err != nil {
		return err
	}

	glassBox.BoxID = getGlassBox[0].BoxID
	if glassBox.InternalName == "" {
		glassBox.InternalName = getGlassBox[0].InternalName
	}

	var updateMeasurements []Measurement
	for _, m := range glassBox.Measurements {
		insertRecord := true
		if m.GlassBoxID == nil {
			m.GlassBoxID = &getGlassBox[0].BoxID
		}
		// compare if new and existing records are identicals
		for _, mm := range getGlassBox[0].Measurements {
			if m.Width == mm.Width && m.Height == mm.Height && m.Thickness == mm.Thickness {
				insertRecord = false
				break
			}
		}
		if insertRecord {
			updateMeasurements = append(updateMeasurements, m)
		}
	}
	glassBox.Measurements = updateMeasurements

	dump.P(glassBox)

	if err := db.Session(&gorm.Session{FullSaveAssociations: true}).Save(&glassBox).Error; err != nil {
		return err
	}

	return nil
}

func DeleteGlassBox(db *gorm.DB, glassBoxNameOrID string) (*GlassBox, error) {
	glassBox, err := GetGlassBox(db, glassBoxNameOrID)
	if err != nil {
		return nil, err
	}

	db.Unscoped().Select("Measurements").Delete(glassBox[0])

	return &glassBox[0], nil
}

func (bluePrint *BluePrint) CreateBluePrint(db *gorm.DB) error {
	transactionError := db.Transaction(func(tx *gorm.DB) error {
		if err := db.Omit("Measurements").Create(&bluePrint).Error; err != nil {
			return err
		}

		for i := range bluePrint.Measurements {
			bluePrint.Measurements[i].BluePrintID = &bluePrint.ID
		}

		// bulk create record in BluePrints for each individual measurement record.
		if err := db.Create(&bluePrint.Measurements).Error; err != nil {
			return err
		}

		return nil
	})
	if transactionError != nil {
		return transactionError
	}

	return nil
}

// GetBluePrint handles both get a BluePrint and get all BluePrints.
func GetBluePrint(db *gorm.DB, bluePrintName string) ([]BluePrint, error) {
	var bluePrints []BluePrint

	if bluePrintName != "" {
		if err := db.Preload("Measurements").First(&bluePrints, "name = ?", bluePrintName); err.Error != nil {
			if errors.Is(err.Error, gorm.ErrRecordNotFound) {
				return nil, fmt.Errorf("Blue print with name:%s not found", bluePrintName)
			}
			return nil, err.Error
		}
	} else {
		if err := db.Preload("Measurements").Find(&bluePrints); err.Error != nil {
			return nil, err.Error
		}
	}

	return bluePrints, nil
}

func (bluePrint *BluePrint) UpdateBluePrint(db *gorm.DB, bluePrintName string) error {
	getBluePrint, err := GetBluePrint(db, bluePrintName)
	if err != nil {
		return err
	}

	bluePrint.ID = getBluePrint[0].ID
	if bluePrint.Name == "" {
		bluePrint.Name = getBluePrint[0].Name
	}

	var newMeasurements []Measurement
	for _, m := range bluePrint.Measurements {
		insertRecord := true
		if m.BluePrintID == nil {
			m.BluePrintID = &getBluePrint[0].ID
		}
		// compare if new and existing records are identicals
		for _, mm := range getBluePrint[0].Measurements {
			if m.Width == mm.Width && m.Height == mm.Height && m.Thickness == mm.Thickness {
				insertRecord = false
				break
			}
		}
		if insertRecord {
			newMeasurements = append(newMeasurements, m)
		}
	}

	bluePrint.Measurements = newMeasurements

	if err := db.Session(&gorm.Session{FullSaveAssociations: true}).Save(&bluePrint).Error; err != nil {
		return err
	}

	return nil
}

func DeleteBluePrint(db *gorm.DB, bluePrintName string) (*BluePrint, error) {
	bluePrint, err := GetBluePrint(db, bluePrintName)
	if err != nil {
		return nil, err
	}

	db.Unscoped().Select("Measurements").Delete(bluePrint[0])

	return &bluePrint[0], nil
}

func CompareBluePrintWithGlassBox(db *gorm.DB, urlParams url.Values) ([]Result, error) {
	var bluePrint BluePrint
	var glassBox GlassBox
	var sqlQuery string
	var err error

	if bpName, ok := urlParams["blueprint"]; ok {
		sqlQuery = fmt.Sprintf("name = '%s'", bpName[0])
		err = db.Where(sqlQuery).Preload("Measurements").First(&bluePrint).Error
	}
	if gbName, ok := urlParams["glassbox"]; ok {
		sqlQuery = fmt.Sprintf("internal_name = '%s'", gbName[0])
		if err = db.Where(sqlQuery).Preload("Measurements").First(&glassBox).Error; err != nil {
			if errors.Is(err, gorm.ErrRecordNotFound) {
				sqlQuery = fmt.Sprintf("box_id = '%s'", gbName[0])
				err = db.Where(sqlQuery).Preload("Measurements").First(&glassBox).Error
			}
		}
	}
	if err != nil && !errors.Is(err, gorm.ErrRecordNotFound) {
		return nil, err
	}

	var results []Result
	if bluePrint.Name != "" {
		for _, measurement := range bluePrint.Measurements {
			sqlQuery = fmt.Sprintf(`
				SELECT gb.box_id, gb.internal_name, m.width, m.height, m.thickness, m.quantity
				FROM measurements m 
				JOIN glass_boxes gb 
				ON gb.box_id = m.glass_box_id 
				WHERE m.width = %d 
				AND m.height = %d 
				AND m.thickness = %d 
				AND m.quantity > 0
				AND m.blue_print_id IS NULL`,
				measurement.Width,
				measurement.Height,
				measurement.Thickness)
			db.Order("gb.internal_name").Raw(sqlQuery).Scan(&results)
		}
	} else {
		for _, measurement := range glassBox.Measurements {
			sqlQuery = fmt.Sprintf(`
				SELECT bp.name, m.width, m.height, m.thickness, m.quantity
				FROM measurements m 
				JOIN blue_prints bp 
				ON bp.id = m.blue_print_id 
				WHERE m.width = %d 
				AND m.height = %d 
				AND m.thickness = %d 
				AND m.quantity > 0
				AND m.glass_box_id IS NULL`,
				measurement.Width,
				measurement.Height,
				measurement.Thickness)
			db.Debug().Order("bp.name").Raw(sqlQuery).Scan(&results)
		}
	}

	return results, nil
}

// TODO: Add color validation
func localnameValidation(localName string) (int, error) {
	idx := strings.Index(localName, "-")
	customError := fmt.Errorf("Localname incorrect format '%s' must be on format 'color-number'", localName)
	if idx == -1 {
		return -1, customError
	}
	if _, err := strconv.Atoi(localName[idx+1:]); err != nil {
		return -1, customError
	}

	return idx, nil
}

func parseMeasurement(line string) (m Measurement, err error) {
	for _, s := range strings.Split(line, " X ") {
		unit := strings.Split(strings.TrimSpace(s), " ")
		if len(unit) != 2 {
			continue
		}

		v, err := strconv.Atoi(unit[0])
		if err != nil {
			return m, err
		}
		switch unit[1] {
		case "W":
			m.Width = v
		case "H":
			m.Height = v
		case "T":
			m.Thickness = v
		}
	}
	if m == (Measurement{}) {
		return m, errors.New("empty")
	}
	return m, nil
}

package utils

import (
	"strconv"
)

// CastStringToUint takes in map parameters as strings and returns
// there uint representation as a slice.
func CastStringToUint(pathParams map[string]string) ([]uint, error) {
	var paramsToUint []uint
	for _, value := range pathParams {
		u64, err := strconv.ParseUint(value, 10, 32)
		if err != nil {
			return nil, err
		}

		paramsToUint = append(paramsToUint, uint(u64))
	}

	return paramsToUint, nil
}

func CastParamToUint(pathParam string) (uint, error) {
	//var paramsToUint []uint
	//for _, value := range pathParams {
	u64, err := strconv.ParseUint(pathParam, 10, 32)
	if err != nil {
		return 0, err
	}

	//paramsToUint = append(paramsToUint, uint(u64))
	//}

	return uint(u64), nil
}

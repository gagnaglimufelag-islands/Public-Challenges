package auth

import (
	"errors"
	"time"
  "crypto/rand"

	"github.com/dgrijalva/jwt-go"
)

var jwtKey, _ = GenSymmetricKey(32) // No hardcoded key for you :P []byte("supersecretkey")

type JWTClaim struct {
	Username string `json:"username"`
	Email    string `json:"email"`
	jwt.StandardClaims
}

func GenerateJWT(email, username string) (tokenString string, err error) {
	expirationTime := time.Now().Add(1 * time.Hour)
	claims := &JWTClaim{
		Email:    email,
		Username: username,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expirationTime.Unix(),
		},
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	tokenString, err = token.SignedString(jwtKey)
	return
}

// ValidateToken returns a user's email and or error based on signedToken,
// so other user's attributes can be retrieved from db.
// Validates as well the token.
func ValidateToken(signedToken string) (string, error) {
	token, err := jwt.ParseWithClaims(
		signedToken,
		&JWTClaim{},
		func(token *jwt.Token) (interface{}, error) {
			return []byte(jwtKey), nil
		},
	)

	if err != nil {
		return "", err
	}

	claims, ok := token.Claims.(*JWTClaim)
	if !ok {
		err = errors.New("Couldn't parse claims")
		return "", err
	}

	if claims.ExpiresAt < time.Now().Local().Unix() {
		err = errors.New("token expired")
		return "", err
	}

	return claims.Email, nil
}

func GenSymmetricKey(bytes int) (k []byte, err error) {
    k = make([]byte, bytes)
    if _, err = rand.Read(k); err != nil {
	    return nil, err
    }

    return k, nil
}

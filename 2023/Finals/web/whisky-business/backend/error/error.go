package error

import (
	"net/http"
)

// Error defines standard error types of rk style
type Error struct {
	Code    int           `json:"code"`    // Code represent codes in response
	Status  string        `json:"status"`  // Status represent string value of code
	Message string        `json:"message"` // Message represent detail message
	Details []interface{} `json:"details"` // Details is a list of details in any types in string
}

// Option is ErrorResp option
type Option func(*ErrorResp)

// ErrorResp is standard rk style error
type ErrorResp struct {
	Err *Error // Err is RK style error type
}

func New(opts ...Option) *ErrorResp {
	resp := &ErrorResp{
		Err: &Error{
			Code:    http.StatusInternalServerError,
			Status:  http.StatusText(http.StatusInternalServerError),
			Details: make([]interface{}, 0),
		},
	}

	for i := range opts {
		opts[i](resp)
	}
	return resp
}

// WithMessage provides messages along with response
func WithMessage(message string) Option {
	return func(resp *ErrorResp) {
		resp.Err.Message = message
	}
}

// WithDetails provides any type of error details into error response
func WithDetails(details ...interface{}) Option {
	return func(resp *ErrorResp) {
		for i := range details {
			detail := details[i]

			switch v := detail.(type) {
			case *Error:
				resp.Err.Details = append(resp.Err.Details, v.Details...)
			case error:
				resp.Err.Details = append(resp.Err.Details, v.Error())
			default:
				resp.Err.Details = append(resp.Err.Details, v)
			}
		}
	}
}

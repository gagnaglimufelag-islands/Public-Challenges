package main

import (
	"log"
	"math/rand"
	"net/http"
)

var flagHeader string

var statusCodes = []int{
	000,
	100,
	101,
	102,
	103,
	201,
	202,
	203,
	204,
	205,
	206,
	207,
	208,
	218,
	226,
	300,
	301,
	302,
	303,
	304,
	305,
	306,
	307,
	308,
	400,
	401,
	402,
	403,
	404,
	405,
	406,
	407,
	408,
	409,
	410,
	411,
	412,
	413,
	414,
	415,
	416,
	417,
	418,
	419,
	420,
	421,
	422,
	423,
	424,
	425,
	426,
	428,
	429,
	430,
	431,
	440,
	444,
	449,
	450,
	451,
	460,
	463,
	464,
	494,
	495,
	496,
	497,
	498,
	499,
	500,
	501,
	502,
	503,
	504,
	505,
	506,
	507,
	508,
	509,
	510,
	511,
	520,
	521,
	522,
	523,
	524,
	525,
	526,
	527,
	529,
	530,
	540,
	561,
	598,
	599,
	783,
}

func getOffMyLawn(w http.ResponseWriter, r *http.Request) {
	httpCode := statusCodes[rand.Intn(len(statusCodes))]

	log.Printf("-> Get off my lawn: %d\n", httpCode)

	http.Error(w, "OK", httpCode)
}

func secretFlagHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "FANI" {
		getOffMyLawn(w, r)
		return
	}

	if r.Header.Get("FLAG") != flagHeader {
		getOffMyLawn(w, r)
		return
	}

	log.Printf("-> OK: %d\n", 200)

	http.ServeFile(w, r, "flag.txt")
}

func rootHandler(w http.ResponseWriter, r *http.Request) {
	getOffMyLawn(w, r)
}

func logger(handler http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		log.Printf("<- %s %s\n", r.Method, r.URL)

		handler.ServeHTTP(w, r)
	})
}

func init() {
	log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile)

	flagHeader = "BANDERA"
}

func main() {
	log.Println("Starting flag server...")

	http.HandleFunc("/", rootHandler)
	http.HandleFunc("/Bandeira", getOffMyLawn)
	http.HandleFunc("/Flagge", getOffMyLawn)
	http.HandleFunc("/Fána", getOffMyLawn)
	http.HandleFunc("/Fändel", getOffMyLawn)
	http.HandleFunc("/bandeira", getOffMyLawn)
	http.HandleFunc("/bandera", getOffMyLawn)
	http.HandleFunc("/bandiera", getOffMyLawn)
	http.HandleFunc("/baner", getOffMyLawn)
	http.HandleFunc("/bratach", getOffMyLawn)
	http.HandleFunc("/drapeau", getOffMyLawn)
	http.HandleFunc("/flag", getOffMyLawn)
	http.HandleFunc("/flaga", getOffMyLawn)
	http.HandleFunc("/flagg", getOffMyLawn)
	http.HandleFunc("/flagga", getOffMyLawn)
	http.HandleFunc("/flagge", getOffMyLawn)
	http.HandleFunc("/flamuri", secretFlagHandler)
	http.HandleFunc("/karogs", getOffMyLawn)
	http.HandleFunc("/lipp", getOffMyLawn)
	http.HandleFunc("/lippu", getOffMyLawn)
	http.HandleFunc("/steag", getOffMyLawn)
	http.HandleFunc("/vlag", getOffMyLawn)
	http.HandleFunc("/vlajka", getOffMyLawn)
	http.HandleFunc("/veliava", getOffMyLawn)
	http.HandleFunc("/zastava", getOffMyLawn)
	http.HandleFunc("/zaszlo", getOffMyLawn)
	http.HandleFunc("/прапо", getOffMyLawn)

	err := http.ListenAndServe(":32000", logger(http.DefaultServeMux))
	if err != nil {
		log.Fatal(err)
	}
}

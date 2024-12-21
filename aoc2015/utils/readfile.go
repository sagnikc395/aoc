package utils

import (
	"log"
	"os"
)

func ReadFile(filename string) []byte {
	// remember to use relative file name
	f, err := os.ReadFile(filename)
	if err != nil {
		log.Fatal("file does not exist")
	}

	return f
}

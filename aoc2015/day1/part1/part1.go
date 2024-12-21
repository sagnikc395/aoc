package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	f, err := os.ReadFile("./input.txt")
	if err != nil {
		log.Fatalf("input file not found")
	}

	data := string(f)
	level := 0
	for _, val := range data {
		if val == '(' {
			level += 1
		} else if val == ')' {
			level -= 1
		}
	}

	fmt.Println(level)

}

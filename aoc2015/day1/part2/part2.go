package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	f, err := os.ReadFile("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	data := string(f)

	firstPosn := 0

	level := 0
	for i, val := range data {
		if val == '(' {
			level += 1
		} else if val == ')' {
			if level < 0 {
				firstPosn = i
				break
			}
			level -= 1
		}
	}

	fmt.Println(firstPosn)

}

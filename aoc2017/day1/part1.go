package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func parseInt(input string) (ans []int) {
	for _, num := range strings.Split(input, "") {
		val, err := strconv.Atoi(num)
		if err != nil {
			log.Fatal(err)
		}
		ans = append(ans, val)
	}
	return ans
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Panicf("Failed to read the file %s", err)
	}
	digits := parseInt(string(data))
	var sum int
	for i := 0; i < len(digits); i++ {
		if digits[i] == digits[(i+1)%len(digits)] {
			sum += digits[i]
		}
	}
	fmt.Println(sum)
}

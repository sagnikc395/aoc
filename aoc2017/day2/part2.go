package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	count := 0
	diff := 0
	for scanner.Scan() {
		var valSl []int
		vals := strings.Split(scanner.Text(), "\t")
		for _, val := range vals {
			v, e := strconv.Atoi(val)
			if e != nil {
				log.Fatal(e)
			}
			valSl = append(valSl, v)
		}
		sort.Ints(valSl)
		for i := 0; i < len(valSl); i++ {
			for j := 0; j < len(valSl); j++ {
				if i != j {
					if valSl[i]%valSl[j] == 0 {
						diff += valSl[i] / valSl[j]
						break
					} else if valSl[j]%valSl[i] == 0 {
						diff += valSl[j] / valSl[i]
						break
					}
				}
			}
		}
		count += diff
	}
	fmt.Println(count)

}

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
		diff = valSl[len(valSl)-1] - valSl[0]
		count += diff
	}
	fmt.Println(count)

}

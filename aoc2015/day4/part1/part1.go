package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
)

const SECRET = "iwrupvqb"

func min5Zeroes(b string) bool {
	return len(b) >= 5 && b[:5] == "00000"
}

func main() {

	index := 0

	for {
		idxStr := strconv.Itoa(index)
		res := SECRET + idxStr
		hash := md5.Sum([]byte(res))
		hexHash := hex.EncodeToString(hash[:])

		if min5Zeroes(hexHash) {
			fmt.Printf("Solution -> %s, index: %d", hexHash, index)
			break
		}

		index++
	}
}

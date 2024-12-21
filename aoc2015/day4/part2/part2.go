package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
)

const SECRET = "iwrupvqb"

func min5Zeroes2(b string) bool {
	return len(b) >= 6 && b[:6] == "000000"
}

func main() {

	index := 0

	for {
		idxStr := strconv.Itoa(index)
		res := SECRET + idxStr
		hash := md5.Sum([]byte(res))
		hexHash := hex.EncodeToString(hash[:])

		if min5Zeroes2(hexHash) {
			fmt.Printf("Solution -> %s, index: %d", hexHash, index)
			break
		}
		if index%100000 == 0 {
			fmt.Printf("Currently at index: %d\n", index)
		}
		index++
	}
}

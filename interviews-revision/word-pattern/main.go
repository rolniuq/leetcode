package main

import (
	"fmt"
	"strings"
)

func wordPattern(pattern string, s string) bool {
	sArr := strings.Fields(s)

	if len(pattern) != len(sArr) {
		return false
	}

	mapP := map[string]string{}
	mapSArr := map[string]string{}

	for i := 0; i < len(pattern); i++ {
		if sArrChar, ok := mapP[string(pattern[i])]; ok {
			if sArrChar != sArr[i] {
				return false
			}
		} else {
			mapP[string(pattern[i])] = sArr[i]
		}

		if pChar, ok := mapSArr[sArr[i]]; ok {
			if pChar != string(pattern[i]) {
				return false
			}
		} else {
			mapSArr[sArr[i]] = string(pattern[i])
		}
	}

	return true
}

func main() {
	fmt.Println(wordPattern("abba", "dog cat cat dog"))
}

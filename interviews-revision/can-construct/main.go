package main

import (
	"fmt"
)

func canConstruct(ransomNote string, magazine string) bool {
	mMap := make(map[string]int)
	for i := 0; i < len(magazine); i++ {
		_, ok := mMap[string(magazine[i])]
		if !ok {
			mMap[string(magazine[i])] = 1
			continue
		}

		mMap[string(magazine[i])]++
	}

	rMap := make(map[string]int)
	for i := 0; i < len(ransomNote); i++ {
		_, ok := rMap[string(ransomNote[i])]
		if !ok {
			rMap[string(ransomNote[i])] = 1
			continue
		}

		rMap[string(ransomNote[i])]++
	}

	for k, v := range rMap {
		m, ok := mMap[k]
		if !ok || (ok && m < v) {
			return false
		}
	}

	return true
}

func main() {
	ransomNote := "aa"
	magazine := "aab"
	fmt.Println(canConstruct(ransomNote, magazine))
}

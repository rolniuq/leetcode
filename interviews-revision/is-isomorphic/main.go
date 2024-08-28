package main

import (
	"fmt"
)

func isIsomorphic(s, t string) bool {
	if len(s) != len(t) {
		return false
	}

	mapS := map[byte]byte{}
	mapT := map[byte]byte{}
	for i := 0; i < len(s); i++ {
		if sv, ok := mapS[s[i]]; ok {
			if sv != t[i] {
				return false
			}
		} else {
			mapS[s[i]] = t[i]
		}

		if tv, ok := mapT[t[i]]; ok {
			if tv != s[i] {
				return false
			}
		} else {
			mapT[t[i]] = s[i]
		}
	}

	return true
}

func main() {
	s := "egg"
	t := "add"

	fmt.Println(isIsomorphic(s, t))
}

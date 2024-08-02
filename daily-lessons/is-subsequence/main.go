package main

import (
	"fmt"
)

func isSubsequence(s, t string) bool {
	if len(s) == 0 {
		return true
	}

	charIndex := 0
	for i := 0; i < len(t); i++ {
		if string(s[charIndex]) == string(t[i]) {
			charIndex++
		}
		if charIndex == len(s) {
			return true
		}
	}

	return false
}

func main() {
	res := isSubsequence("abc", "ahbgdc")
	fmt.Println(res)
}

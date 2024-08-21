package main

import "fmt"

func isSubsequence(s string, t string) bool {
	if len(s) == 0 {
		return true
	}

	charIndex := 0
	for _, v := range t {
		if string(s[charIndex]) == string(v) {
			charIndex++
		}
		if charIndex == len(s) {
			return true
		}
	}

	return false
}

func main() {
	s := "abc"
	t := "ahbgdc"
	fmt.Println(isSubsequence(s, t))
}

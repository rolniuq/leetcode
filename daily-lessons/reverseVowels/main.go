package main

import (
	"fmt"
	"strings"
)

func reverseVowels(s string) string {
	vowels := "aeiouAEIOU"

	arr := []string{}
	for i := len(s) - 1; i >= 0; i-- {
		if strings.Contains(vowels, string(s[i])) {
			arr = append(arr, string(s[i]))
		}
	}

	fmt.Println(arr)

	for i := 0; i < len(s); i++ {
		if len(arr) != 0 && strings.Contains(vowels, string(s[i])) {
			s = s[:i] + arr[0] + s[i+1:]
			arr = arr[1:]
		}
	}

	return s
}

func main() {
	res := reverseVowels("aA")
	fmt.Println(res)
}

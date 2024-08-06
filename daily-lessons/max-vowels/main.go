package main

import (
	"fmt"
	"strings"
)

func countVowels(s string) int {
	count := 0
	vowels := "aeiouAEIOU"

	for i := 0; i < len(s); i++ {
		if strings.Contains(vowels, string(s[i])) {
			count++
		}
	}

	return count
}

func maxVowels(s string, k int) int {
	vowels := "aeiouAEIOU"
	subStr := s[0:k]
	count := countVowels(subStr)
	max := count

	for i := k; i < len(s); i++ {
		firstChar := string(subStr[0])
		if strings.Contains(vowels, firstChar) {
			count--
		}
		if strings.Contains(vowels, string(s[i])) {
			count++
		}
		if count > max {
			max = count
		}

		subStr = subStr[1:] + string(s[i])
	}

	return max
}

func main() {
	s := "abciiidef"
	k := 3
	res := maxVowels(s, k)
	fmt.Println(res)
}

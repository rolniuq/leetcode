package main

import (
	"fmt"
	"strings"
)

func reverseWords(s string) string {
	words := strings.Fields(s)

	res := words[len(words)-1]
	for i := len(words) - 2; i >= 0; i-- {
		res = res + " " + words[i]
	}

	return res
}

func main() {
	res := reverseWords("the sky is blue")
	fmt.Println(res == "blue is sky the")
}

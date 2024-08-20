package main

import (
	"fmt"
	"strings"
)

func reverseWords(s string) string {
	str := strings.Fields(s)

	res := str[len(str)-1]
	for i := len(str) - 2; i >= 0; i-- {
		res += " " + str[i]
	}

	return res
}

func main() {
	res := reverseWords("  hello world  ")
	fmt.Println(res)
}

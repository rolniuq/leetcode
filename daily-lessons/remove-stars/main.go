package main

import (
	"fmt"
)

func removeStars(s string) string {
	res := ""
	skip := 0

	for i := len(s) - 1; i >= 0; i-- {
		if string(s[i]) == "*" {
			skip++
			continue
		}

		if skip > 0 {
			skip--
			continue
		}

		res = string(s[i]) + res
	}

	return res
}

func main() {
	s := "leet**cod*e"
	res := removeStars(s)
	fmt.Println(res)
}

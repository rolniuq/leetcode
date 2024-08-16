package main

import (
	"fmt"
	"strings"
)

func longestCommonPrefix(strs []string) string {
	minLength := len(strs[0])
	for _, str := range strs {
		if len(str) == 0 {
			return ""
		}
		if len(str) < minLength {
			minLength = len(str)
		}
	}

	max := ""
	res := ""
	start := 0
	for start < minLength {
		res += string(strs[0][start])

		included := true
		for i := 1; i < len(strs); i++ {
			if !strings.HasPrefix(strs[i], res) {
				included = false
				break
			}
		}

		if included {
			if len(max) < len(res) {
				max = res
			}
		}

		start++
	}

	return max
}

func main() {
	strs := []string{"flower", "flow", "flight"}
	res := longestCommonPrefix(strs)
	fmt.Println(res)
}

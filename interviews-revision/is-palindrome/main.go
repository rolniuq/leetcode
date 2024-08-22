package main

import (
	"fmt"
	"strings"
)

func isPalindrome(s string) bool {
	str := ""
	s = strings.ToLower(s)
	for _, v := range s {
		cur := string(v)
		if "0" <= cur && cur <= "9" || "a" <= cur && cur <= "z" {
			str += cur
		}
	}

	left := 0
	right := len(str) - 1
	for left <= right {
		l := string(str[left])
		r := string(str[right])
		if l != r {
			return false
		}

		left++
		right--
	}

	return true
}

func main() {
	s := "A man, a plan, a canal: Panama"
	res := isPalindrome(s)
	fmt.Println(res)
}

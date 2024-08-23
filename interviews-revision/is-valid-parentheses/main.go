package main

import (
	"fmt"
	"strings"
)

func isValid(s string) bool {
	stack := []string{}
	for i := 0; i < len(s); i++ {
		c := string(s[i])
		if strings.Contains("])}", c) {
			if c == "]" && len(stack) > 0 {
				if stack[len(stack)-1] != "[" {
					return false
				}

				stack = stack[:len(stack)-1]
			} else if c == ")" && len(stack) > 0 {
				if stack[len(stack)-1] != "(" {
					return false
				}

				stack = stack[:len(stack)-1]
			} else if c == "}" && len(stack) > 0 {
				if stack[len(stack)-1] != "{" {
					return false
				}

				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			stack = append(stack, c)
		}
	}

	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("{[]}"))
}


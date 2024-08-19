package main

import (
	"fmt"
	"strconv"
)

func decodeString(s string) string {
	res := ""
	curNum := 0
	stack := []string{}

	for i := 0; i < len(s); i++ {
		curStr := string(s[i])

		if curStr >= "0" && curStr <= "9" {
			num, _ := strconv.Atoi(curStr)
			curNum = curNum*10 + num
		} else if curStr == "[" {
			stack = append(stack, res)
			stack = append(stack, strconv.Itoa(curNum))

			curNum = 0
			res = ""
		} else if curStr == "]" {
			numStr := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			previosStr := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			num, _ := strconv.Atoi(numStr)
			str := ""
			for j := 0; j < num; j++ {
				str += res
			}

			res = previosStr + str
		} else {
			res += curStr
		}
	}

	return res
}

func main() {
	s := "3[a]2[bc]"
	res := decodeString(s)
	fmt.Println(res)
}

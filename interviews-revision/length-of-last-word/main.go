package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(s string) int {
	arr := strings.Fields(s)

	return len(arr[len(arr)-1])
}

func main() {
	res := lengthOfLastWord("   fly me   to   the moon  ")
	fmt.Println(res)
}

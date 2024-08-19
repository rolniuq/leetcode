package main

import "fmt"

// Find the Index of the First Occurrence in a String
func strStr(haystack string, needle string) int {
	left := 0

	for left+len(needle) <= len(haystack) {
		temp := haystack[left : left+len(needle)]
		if temp == needle {
			return left
		}

		left++
	}

	return -1
}

func main() {
	haystack := "sadbutsad"
	needle := "sad"

	fmt.Println(strStr(haystack, needle))
}

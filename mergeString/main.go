package main

import "fmt"

func mergeAlternately(word1 string, word2 string) string {
	res := ""
	redundant := ""

	if len(word1) == 0 {
		return word2
	}

	if len(word2) == 0 {
		return word1
	}

	if len(word1) > len(word2) {
		redundant = word1[len(word2):]
		word1 = word1[:len(word2)]
	}
	if len(word1) < len(word2) {
		redundant = word2[len(word1):]
		word2 = word2[:len(word1)]
	}

	for i := 0; i < len(word1); i++ {
		res = res + string(word1[i]) + string(word2[i])
	}

	res = res + redundant

	return res
}

func main() {
	res := mergeAlternately("abc", "pd")
	fmt.Println(res)
}

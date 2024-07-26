package main

import "fmt"

func maxRepeating(sequence string, word string) int {
	max := 0
	count := 0
	for i := 0; i < len(sequence); i++ {
		if i+len(word) <= len(sequence) {
			substr := sequence[i : i+len(word)]
			if substr == word {
				count++
				i += len(word) - 1
			} else {
				i -= count * len(word)
				count = 0
			}
		}

		if max <= count {
			max = count
		}
	}

	return max
}

func main() {
	res := maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba")
	fmt.Println(res)
}

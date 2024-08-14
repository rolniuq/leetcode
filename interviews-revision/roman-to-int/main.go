package main

import (
	"fmt"
	"strings"
)

// I can be placed before V (5) and X (10) to make 4 and 9.
// X can be placed before L (50) and C (100) to make 40 and 90.
// C can be placed before D (500) and M (1000) to make 400 and 900.

func romanToInt(s string) int {
	charCanReplaced := "IXC"
	mapRoman := map[string]int{
		"I":  1,
		"IV": 4,
		"V":  5,
		"IX": 9,
		"X":  10,
		"XL": 40,
		"L":  50,
		"XC": 90,
		"C":  100,
		"CD": 400,
		"D":  500,
		"CM": 900,
		"M":  1000,
	}

	res := 0
	for i := 0; i < len(s); i++ {
		char := string(s[i])
		if i < len(s)-1 && strings.Contains(charCanReplaced, char) {
			extendChar := string(s[i]) + string(s[i+1])
			_, ok := mapRoman[extendChar]
			if ok {
				char = extendChar
				i++
			}
		}

		res += mapRoman[char]
	}

	return res
}

func main() {
	res := romanToInt("MCMXCIV")
	fmt.Println(res)
}

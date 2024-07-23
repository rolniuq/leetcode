package main

import "fmt"

func gcd(a, b int) int {
	if a == b {
		return a
	} else if a < b {
		return gcd(a, b-a)
	}

	return gcd(a-b, b)
}

func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}

	gcdValue := gcd(len(str1), len(str2))

	return str1[:gcdValue]
}

func main() {
	str1 := "ABABAB"
	str2 := "ABAB"

	res := gcdOfStrings(str1, str2)
	fmt.Println(res)
}

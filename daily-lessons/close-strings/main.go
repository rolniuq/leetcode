package main

import (
	"fmt"
	"reflect"
	"sort"
)

func getCharFrequency(s string) map[rune]int {
	res := map[rune]int{}

	for _, v := range s {
		_, ok := res[v]
		if !ok {
			res[v] = 0
			continue
		}

		res[v]++
	}

	return res
}

func getCharUnique(s string) []string {
	mapChar := map[rune]bool{}
	for _, v := range s {
		_, ok := mapChar[v]
		if !ok {
			mapChar[v] = true
		}
	}

	res := []string{}
	for c := range mapChar {
		res = append(res, string(c))
	}

	sort.Slice(res, func(i, j int) bool {
		return res[i] < res[j]
	})

	return res
}

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}

	if !reflect.DeepEqual(getCharUnique(word1), getCharUnique(word2)) {
		return false
	}

	mapChar1 := getCharFrequency(word1)
	mapChar2 := getCharFrequency(word2)

	var value1, value2 []int
	for _, v := range mapChar1 {
		value1 = append(value1, v)
	}
	for _, v := range mapChar2 {
		value2 = append(value2, v)
	}

	sort.Ints(value1)
	sort.Ints(value2)

	return reflect.DeepEqual(value1, value2)
}

func main() {
	word1 := "abc"
	word2 := "bca"
	res := closeStrings(word1, word2)
	fmt.Println(res)
}

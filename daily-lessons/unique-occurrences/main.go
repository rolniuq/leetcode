package main

import "fmt"

func uniqueOccurrences(arr []int) bool {
	mapArr := map[int]int{}
	for _, v := range arr {
		_, ok := mapArr[v]
		if !ok {
			mapArr[v] = 0
		} else {
			mapArr[v]++
		}
	}

	mapValue := map[int]bool{}
	arrValue := []int{}
	for _, v := range mapArr {
		arrValue = append(arrValue, v)
		_, ok := mapValue[v]
		if !ok {
			mapValue[v] = true
		}
	}

	arrValue2 := []int{}
	for k := range mapValue {
		arrValue2 = append(arrValue2, k)
	}

	return len(arrValue2) == len(arrValue)
}

func main() {
	arr := []int{1, 2, 2, 1, 1, 3}
	res := uniqueOccurrences(arr)
	fmt.Println(res)
}

package main

import "fmt"

func majorityElement(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	mapCounter := map[int]int{}
	for _, num := range nums {
		_, ok := mapCounter[num]
		if !ok {
			mapCounter[num] = 1
		} else {
			mapCounter[num]++
		}
	}

	max := 1
	maxIndex := 0
	for i, count := range mapCounter {
		if count > max {
			max = count
			maxIndex = i
		}
	}

	return maxIndex
}

func main() {
	nums := []int{3, 2, 3}
	res := majorityElement(nums)
	fmt.Println(res)
}

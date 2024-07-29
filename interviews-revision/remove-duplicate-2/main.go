package main

import (
	"fmt"
)

func removeDuplicates(nums []int) int {
	total := 1
	count := 1

	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			nums[total] = nums[i]
			total++
			count = 1

			continue
		}

		if count < 2 {
			nums[total] = nums[i]
			total++
			count++
		}
	}

	return total
}

func main() {
	nums := []int{0, 0, 1, 1, 1, 1, 2, 3, 3}
	res := removeDuplicates(nums)
	fmt.Println(nums, res)
}

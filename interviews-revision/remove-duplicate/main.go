package main

import "fmt"

func removeDuplicates(nums []int) int {
	count := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			continue
		}

		nums[count] = nums[i]
		count++
	}

	return count
}

func main() {
	nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	res := removeDuplicates(nums)
	fmt.Println(nums, res)
}

package main

import (
	"fmt"
	"sort"
)

// give an integer array, and k
// remove all element which sum of 2 equal k

func maxOperations(nums []int, k int) int {
	sort.Ints(nums)

	count := 0

	left := 0
	right := len(nums) - 1

	for {
		if left >= right {
			return count
		}

		sum := nums[left] + nums[right]
		if sum == k {
			count++
			left++
			right--
		} else if nums[left]+nums[right] > k {
			right--
		} else {
			left++
		}
	}
}

func main() {
	nums := []int{1, 2, 3, 4}
	res := maxOperations(nums, 5)
	fmt.Println(res)
}

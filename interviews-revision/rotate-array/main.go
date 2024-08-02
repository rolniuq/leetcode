package main

import "fmt"

func addFirst(nums []int, value int) {
	for i := len(nums) - 1; i > 0; i-- {
		nums[i] = nums[i-1]
	}

	nums[0] = value
}

func rotate(nums []int, k int) {
	for i := 0; i < k; i++ {
		addFirst(nums, nums[len(nums)-1])
	}
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7}

	rotate(nums, 3)
	fmt.Println(nums)
}

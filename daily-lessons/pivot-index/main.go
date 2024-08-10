package main

import "fmt"

func sum(nums []int) int {
	sum := 0

	for _, v := range nums {
		sum += v
	}

	return sum
}

func pivotIndex(nums []int) int {
	left := 0
	right := len(nums) - 1
	pivot := 0

	for pivot <= right {
		leftSum := sum(nums[left:pivot])
		rightSum := sum(nums[pivot+1:])

		if leftSum == rightSum {
			return pivot
		}

		pivot++
	}

	return -1
}

func main() {
	nums := []int{-1, -1, 0, -1, -1, -1}
	res := pivotIndex(nums)
	fmt.Println(res)
}

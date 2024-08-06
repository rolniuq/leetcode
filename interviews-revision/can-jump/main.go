package main

import "fmt"

func canJump(nums []int) bool {
	count := 0

	for i := 0; i < len(nums); i++ {
		if count < i {
			return false
		}

		if count < nums[i]+i {
			count = nums[i] + i
		}
	}

	return true
}

func main() {
	nums := []int{2, 3, 1, 1, 4}
	res := canJump(nums)
	fmt.Println(res)
}

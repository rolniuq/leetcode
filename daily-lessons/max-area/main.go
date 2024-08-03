package main

import (
	"fmt"
)

func getHeight(a, b int) int {
	if a > b {
		return b
	}

	return a
}

func maxArea(nums []int) int {
	max := 0
	left := 0
	right := len(nums) - 1

	for {
		if left >= right {
			return max
		}

		mul := (right - left) * getHeight(nums[left], nums[right])
		if max < mul {
			max = mul
		}

		if nums[left] < nums[right] {
			left++
		} else {
			right--
		}
	}
}

func main() {
	h := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	res := maxArea(h)
	fmt.Println(res)
}

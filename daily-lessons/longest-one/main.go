package main

import "fmt"

func longestOne(nums []int, k int) int {
	maxLen := 0
	curLen := 0
	exist := k

	start := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			exist--
		}

		if exist >= 0 {
			curLen++
		} else {
			for nums[start] != 0 {
				start++
				curLen--
			}
			start++
			exist++
		}

		if curLen > maxLen {
			maxLen = curLen
		}
	}

	return maxLen
}

func main() {
	nums := []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}
	k := 2
	res := longestOne(nums, k)
	fmt.Println(res)
}

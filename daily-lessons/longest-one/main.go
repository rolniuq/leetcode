package main

import "fmt"

func longestOne(nums []int, k int) int {
	start := 0
	end := 0
	max := 0

	temp := k
	for i := 0; i < len(nums); i++ {
		if temp == 0 {
			fmt.Println(start, end)
			curmax := len(nums[start:end])
			if curmax > max {
				max = curmax
			}
			temp = k
		}
		if nums[i] == 1 && start == 0 {
			start = i
		} else if temp > 0 {
			end = i
			temp--
		}
	}

	return len(nums[start:end])
}

func main() {
	nums := []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}
	k := 2
	res := longestOne(nums, k)
	fmt.Println(res)
}

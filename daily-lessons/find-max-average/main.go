package main

import (
	"fmt"
)

func sum(arr []int) int {
	total := 0
	for i := 0; i < len(arr); i++ {
		total += arr[i]
	}

	return total
}

func average(sum int, size int) float64 {
	return float64(sum) / float64(size)
}

func findMaxAverage(nums []int, k int) float64 {
	if len(nums) == 1 {
		return float64(nums[0])
	}

	curSum := sum(nums[0:k])

	maxSum := curSum
	for i := k; i < len(nums); i++ {
		curSum = curSum + nums[i] - nums[i-k]
		if curSum > maxSum {
			maxSum = curSum
		}
	}

	return average(maxSum, k)
}

func main() {
	nums := []int{0, 1, 1, 3, 3}
	k := 4
	res := findMaxAverage(nums, k)
	fmt.Println(res)
}

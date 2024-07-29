package main

import "fmt"

func productExceptSelf(nums []int) []int {
	res := make([]int, len(nums))

	mul := 1
	for i := 0; i < len(nums); i++ {
		res[i] = mul
		mul *= nums[i]
	}

	temp := 1
	for i := len(nums) - 1; i >= 0; i-- {
		res[i] *= temp
		temp *= nums[i]
	}

	return res
}

func main() {
	res := productExceptSelf([]int{1, 2, 3, 4})
	fmt.Println(res)
}

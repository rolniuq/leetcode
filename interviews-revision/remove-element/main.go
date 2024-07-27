package main

import "fmt"

func removeElement(nums []int, val int) int {
	c := 0

	for _, v := range nums {
		if v != val {
			nums[c] = v
			c++
		}
	}

	fmt.Println(nums)
	return c
}

func main() {
	res := removeElement([]int{3, 2, 2, 3}, 3)
	fmt.Println(res == 2)
}

package main

import (
	"fmt"
)

func asteroidCollision(nums []int) []int {
	res := []int{}
	for i := 0; i < len(nums); i++ {
		cur := nums[i]
		if cur > 0 {
			res = append(res, cur)
		} else {
			for len(res) > 0 && res[len(res)-1] > 0 && res[len(res)-1] < -cur {
				res = res[:len(res)-1]
			}

			if len(res) > 0 && res[len(res)-1] == -cur {
				res = res[:len(res)-1]
				continue
			}

			if len(res) == 0 || res[len(res)-1] < 0 {
				res = append(res, cur)
			}
		}
	}

	return res
}

func main() {
	nums := []int{-2, -1, 1, 2}
	res := asteroidCollision(nums)
	fmt.Println(res)
}

package main

import (
	"fmt"
	"math"
)

// tìm 3 số trong mảng từ trái qua phải
// làm sao cho 3 số đó theo thứ tự từ bé đến lớn
// i < k < l

func increasingTriplet(nums []int) bool {
	smallest := nums[0]
	middle := math.MaxInt64

	for _, num := range nums {
		if num <= smallest {
			smallest = num
		} else if num <= middle {
			middle = num
		}
		if smallest < num && middle < num {
			return true
		}
	}

	return false
}

func main() {
	res := increasingTriplet([]int{20, 100, 10, 12, 5, 13})
	fmt.Println(res)
}

package main

import "fmt"

// find an element != 0, replace it to the insert position

func moveZeros(nums []int) {
	if len(nums) == 0 {
		return
	}

	insertPosition := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			// prevent failed if there is no change: [1, 0]
			if i > insertPosition {
				nums[insertPosition] = nums[i]
				nums[i] = 0
			}

			insertPosition++
		}
	}

	fmt.Println(nums)
}

func main() {
	nums := []int{0, 1, 0, 3, 12}
	moveZeros(nums)
}

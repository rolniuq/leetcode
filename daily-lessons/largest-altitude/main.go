package main

import "fmt"

func largestAltitude(gain []int) int {
	max := 0
	arr := []int{0}
	for i := 0; i < len(gain); i++ {
		cur := gain[i] + arr[i]
		if cur > max {
			max = cur
		}
		arr = append(arr, gain[i]+arr[i])
	}
	return max
}

func main() {
	gain := []int{-5, 1, 5, 0, -7}
	res := largestAltitude(gain)
	fmt.Println(res)
}

package main

import (
	"fmt"
)

// appen daily profit
// [7,1,5,3,6,4] -> dễ dàng nhìn thấy
// 1 - 7 = -6 -> gán = 0
// 5 - 1 = 4 -> ok
// 3 - 5 = =2 -> gán = 0
// 6 - 3 = 3 -> ok
// 4 - 6 = -2 -> gán bằng 0
// -> result = 4 + 3 = 7 -> DPCM

func maxProfit(prices []int) int {
	totalProfit := 0
	for i := 1; i < len(prices); i++ {
		dailyProfit := prices[i] - prices[i-1]

		if dailyProfit < 0 {
			dailyProfit = 0
		}
		totalProfit += dailyProfit
	}

	return totalProfit
}

func main() {
	prices := []int{2, 1, 2, 0, 1}
	res := maxProfit(prices)
	fmt.Println(res)
}

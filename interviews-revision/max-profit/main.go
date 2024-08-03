package main

import (
	"fmt"
	"math"
)

//best time to buy a sell stock

func maxProfit(prices []int) int {
	buy := math.MaxInt64

	profit := 0

	for i := 0; i < len(prices); i++ {
		if prices[i] < buy {
			buy = prices[i]
		}

		currentProfit := prices[i] - buy
		if currentProfit > profit {
			profit = currentProfit
		}
	}

	return profit
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	res := maxProfit(prices)
	fmt.Println(res)
}

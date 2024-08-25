package main

import (
	"fmt"
	"strings"
)

func equalPairs(grid [][]int) int {
	n := len(grid)
	rowMap := make(map[string]int)
	count := 0

	for i := 0; i < n; i++ {
		rowKey := strings.Trim(strings.Join(strings.Fields(fmt.Sprint(grid[i])), ","), "[]")
		rowMap[rowKey]++
	}

	for j := 0; j < n; j++ {
		var col []int
		for i := 0; i < n; i++ {
			col = append(col, grid[i][j])
		}
		colKey := strings.Trim(strings.Join(strings.Fields(fmt.Sprint(col)), ","), "[]")

		if freq, exists := rowMap[colKey]; exists {
			count += freq
		}
	}

	return count
}

func main() {
	grid := [][]int{{3, 2, 1}, {1, 7, 6}, {2, 7, 7}}
	fmt.Println(equalPairs(grid))
}

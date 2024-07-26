package main

import "fmt"

func canPlaceFlowers(flowerbed []int, n int) bool {
	for i := 0; i < len(flowerbed); i++ {
		if flowerbed[i] == 1 {
			continue
		}

		if (i == 0 || flowerbed[i-1] == 0) && (i == len(flowerbed)-1 || flowerbed[i+1] == 0) {
			flowerbed[i] = 1
			n--
		}
	}

	return n <= 0
}
func main() {
	flowerbed := []int{1, 0, 0, 0, 1}
	n := 1
	res := canPlaceFlowers(flowerbed, n)
	fmt.Println(res)
}

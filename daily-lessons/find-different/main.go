package main

import "fmt"

func getMapDistinct(nums1 []int, nums2 []int) map[int]bool {
	m1 := map[int]bool{}
	for _, v := range nums1 {
		m1[v] = true
	}

	res := map[int]bool{}
	for _, v := range nums2 {
		if m1[v] {
			res[v] = true
		}
	}

	return res
}

func removeValid(nums []int, mapDistinct map[int]bool) []int {
	res := []int{}
	mapRes := map[int]bool{}
	for _, v := range nums {
		_, ok := mapDistinct[v]
		_, ok1 := mapRes[v]
		if !ok && !ok1 {
			mapRes[v] = true
			res = append(res, v)
		}
	}

	return res
}

func findDifference(nums1 []int, nums2 []int) [][]int {
	mapDistinct := getMapDistinct(nums1, nums2)
	if mapDistinct == nil {
		return nil
	}

	res := [][]int{}
	res = append(res, removeValid(nums1, mapDistinct))
	res = append(res, removeValid(nums2, mapDistinct))

	return res
}

func main() {
	nums1 := []int{1, 2, 3, 3}
	nums2 := []int{1, 1, 2, 2}
	res := findDifference(nums1, nums2)
	fmt.Println(res)
}

package main

import (
	"fmt"

	listnode "github.com/rolniuq/mypackage/list-node"
)

func pairSum(head *listnode.ListNode) int {
	max := 0
	cur := head
	arr := []int{}
	for cur != nil {
		arr = append(arr, cur.Val)
		cur = cur.Next
	}

	for i := 0; i < len(arr)/2; i++ {
		sum := arr[i] + arr[len(arr)-1-i]
		if sum > max {
			max = sum
		}
	}

	return max
}

func main() {
	values := []int{5, 4, 2, 1}
	l := &listnode.ListNode{}
	l = l.Create(values)

	res := pairSum(l)
	fmt.Println(res)
}

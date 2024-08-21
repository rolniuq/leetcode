package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func createListNode(values []int) *ListNode {
	if len(values) == 0 {
		return nil
	}

	head := &ListNode{Val: values[0]}
	current := head

	for i := 1; i < len(values); i++ {
		current.Next = &ListNode{Val: values[i]}
		current = current.Next
	}

	return head
}

func deleteMiddle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}

	slow := head
	fast := head
	var prev *ListNode

	for fast != nil && fast.Next != nil {
		prev = slow
		slow = slow.Next
		fast = fast.Next.Next
	}

	if prev != nil {
		prev.Next = slow.Next
	}

	return head
}

func main() {
	list := []int{1, 3, 4, 7, 1, 2, 6}
	listNode := createListNode(list)

	res := deleteMiddle(listNode)
	for res != nil {
		fmt.Println(res.Val)
		res = res.Next
	}
}

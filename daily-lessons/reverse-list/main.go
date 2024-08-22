package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func createLinkedList(values []int) *ListNode {
	head := &ListNode{Val: values[0]}
	current := head

	for i := 1; i < len(values); i++ {
		current.Next = &ListNode{Val: values[i]}
		current = current.Next
	}

	return head
}

func (l *ListNode) printLinkedList() {
	if l == nil {
		return
	}

	for l != nil {
		fmt.Println(l.Val)
		l = l.Next
	}
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	current := head

	for current != nil {
		// store next
		next := current.Next
		// reverse current node to prev pointer
		current.Next = prev

		prev = current
		current = next
	}

	return prev
}

func main() {
	values := []int{1, 2, 3, 4, 5}
	listNode := createLinkedList(values)
	res := reverseList(listNode)
	res.printLinkedList()
}

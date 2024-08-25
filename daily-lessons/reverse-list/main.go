package main

import (
	listnode "github.com/rolniuq/mypackage/list-node"
)

func reverseList(head *listnode.ListNode) *listnode.ListNode {
	var prev *listnode.ListNode
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
	l := &listnode.ListNode{}
	l = l.Create(values)
	l = reverseList(l)
	l.Print()
}

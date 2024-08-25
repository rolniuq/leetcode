package main

import (
	listnode "github.com/rolniuq/mypackage/list-node"
)

func deleteMiddle(head *listnode.ListNode) *listnode.ListNode {
	if head == nil || head.Next == nil {
		return nil
	}

	slow := head
	fast := head
	var prev *listnode.ListNode

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
	l := &listnode.ListNode{}
	l = l.Create(list)
	l = deleteMiddle(l)
	l.Print()
}

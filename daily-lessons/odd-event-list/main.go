package main

import listnode "github.com/rolniuq/mypackage/list-node"

func oddEventList(head *listnode.ListNode) *listnode.ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	evenHead := head.Next
	even := head.Next
	odd := head

	for even != nil && even.Next != nil {
		odd.Next = even.Next
		odd = odd.Next

		even.Next = odd.Next
		even = even.Next
	}

	odd.Next = evenHead

	return head
}

func main() {
	values := []int{1, 2, 3, 4, 5}
	l := &listnode.ListNode{}
	l = l.Create(values)

	l = oddEventList(l)

	l.Print()
}

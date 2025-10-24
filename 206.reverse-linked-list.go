/*
 * @lc app=leetcode id=206 lang=golang
 *
 * [206] Reverse Linked List
 */

package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	cur := head
	var prev *ListNode
	for cur != nil {
		nextTmp := cur.Next
		cur.Next = prev
		prev = cur
		cur = nextTmp
	}

	return prev
}

// @lc code=end

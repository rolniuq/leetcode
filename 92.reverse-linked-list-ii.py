#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        reverse_prev = prev
        curHead = prev.next
        prev = None

        for _ in range(right - left + 1):
            nextTmp = curHead.next
            curHead.next = prev
            prev = curHead
            curHead = nextTmp

        reverse_prev.next.next = curHead
        reverse_prev.next = prev

        return dummy.next


# @lc code=end

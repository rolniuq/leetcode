#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def append(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return ListNode(val)

        cur = head
        while cur.next is not None:
            cur = cur.next

        cur.next = ListNode(val)

        return head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = None
        cur = head
        while cur is not None:
            if cur.val != val:
                new_head = self.append(new_head, cur.val)

            cur = cur.next

        return new_head


# @lc code=end

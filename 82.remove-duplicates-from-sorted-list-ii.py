#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        new_head = None
        tail = new_head
        while cur:
            if cur.next is None or cur.val != cur.next.val:
                if new_head is None:
                    new_head = cur
                else:
                    tail.next = cur

                next = cur.next
                tail = cur
                tail.next = None
                cur = next

            else:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
        return new_head


# @lc code=end

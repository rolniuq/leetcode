#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
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
        ref = cur
        while cur != None:
            if cur.next is not None and cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        head = ref

        return head
# @lc code=end


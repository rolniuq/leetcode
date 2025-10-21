#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        while cur:
            if cur.next:
                cur.val, cur.next.val = cur.next.val, cur.val
                cur = cur.next.next
            else:
                cur = cur.next

        return head


# @lc code=end

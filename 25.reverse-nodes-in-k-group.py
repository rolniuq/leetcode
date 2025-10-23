#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getK(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # reverse
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    # will get node kth
    def getK(self, cur: Optional[ListNode], k: int):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur


# @lc code=end

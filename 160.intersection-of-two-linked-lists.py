#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        arrA = []
        curA = headA
        while curA is not None:
            arrA.append(curA)
            curA = curA.next

        curB = headB
        while curB is not None:
            if curB in arrA:
                return curB
            curB = curB.next

        return None


# @lc code=end

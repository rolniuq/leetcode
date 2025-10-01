#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt = ListNode()
        lt_next = lt
        gt = ListNode()
        gt_next = gt

        cur = head
        while cur:
            node = ListNode(cur.val)
            if cur.val >= x:
                # to gt
                gt_next.next = node
                gt_next = gt_next.next
            else:
                # to lt
                lt_next.next = node
                lt_next = lt_next.next

            cur = cur.next

        lt_next.next = gt.next

        return lt.next


# @lc code=end

#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = va
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        arr = []
        while cur is not None:
            arr.append(cur)
            cur = cur.next

        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left].val != arr[right].val:
                return False
            left += 1
            right -= 1

        return True


# @lc code=end

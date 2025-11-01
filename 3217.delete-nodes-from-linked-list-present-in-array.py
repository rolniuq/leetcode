#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
#
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/
#
# algorithms
# Medium (68.52%)
# Likes:    842
# Dislikes: 41
# Total Accepted:    242.1K
# Total Submissions: 353.4K
# Testcase Example:  '[1,2,3]\n[1,2,3,4,5]'
#
# You are given an array of integers nums and the head of a linked list. Return
# the head of the modified linked list after removing all nodes from the linked
# list that have a value that exists in nums.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3], head = [1,2,3,4,5]
#
# Output: [4,5]
#
# Explanation:
#
#
#
# Remove the nodes with values 1, 2, and 3.
#
#
# Example 2:
#
#
# Input: nums = [1], head = [1,2,1,2,1,2]
#
# Output: [2,2,2]
#
# Explanation:
#
#
#
# Remove the nodes with value 1.
#
#
# Example 3:
#
#
# Input: nums = [5], head = [1,2,3,4]
#
# Output: [1,2,3,4]
#
# Explanation:
#
#
#
# No node has value 5.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# All elements in nums are unique.
# The number of nodes in the given list is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
# The input is generated such that there is at least one node in the linked
# list that has a value not present in nums.
#
#
#


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head:
            return None

        # timeout cuz there are a lot of duplicate numbers
        nums_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        cur = dummy

        while cur.next:
            if cur.next.val in nums_set:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val: int):
        if not self.head:
            self.head = ListNode(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)


def createLinkedList(arr: List[int]) -> ListNode:
    linkedList = LinkedList()

    for item in arr:
        linkedList.append(item)

    return linkedList.head


def run():
    testCases = [
        # {"nums": [1, 2, 3], "arr": [1, 2, 3, 4, 5]},
        {"nums": [1], "arr": [1, 2, 1, 2, 1, 2]},
    ]

    for testCase in testCases:
        head = createLinkedList(testCase.get("arr"))

        s = Solution()
        node = s.modifiedList(testCase.get("nums"), head)
        while node:
            print("[SOLUTION]:", node.val)
            node = node.next

        print("\n==========")


run()


# @lc code=end

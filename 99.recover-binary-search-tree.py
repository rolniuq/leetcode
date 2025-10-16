#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List
import math


class Solution:
    def in_order(self, root: Optional[TreeNode]):
        if not root:
            return

        temp = root

        self.in_order(root.left)
        if self.prev and self.prev.val > root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = temp
        self.in_order(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.first = self.second = self.prev = None

        self.in_order(root)

        if self.first:
            self.first.val, self.second.val = self.second.val, self.first.val


# @lc code=end

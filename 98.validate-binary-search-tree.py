#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from typing import Optional


class Solution:
    def validate(self, root: Optional[TreeNode], lower: float, upper: float) -> bool:
        if not root:
            return True

        if not (lower < root.val < upper):
            return False

        return self.validate(root.left, lower, root.val) and self.validate(
            root.right, root.val, upper
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.validate(root.left, -math.inf, root.val) and self.validate(
            root.right, root.val, math.inf
        )


# @lc code=end

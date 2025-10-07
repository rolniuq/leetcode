#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        return (
            abs(left - right) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )


# @lc code=end

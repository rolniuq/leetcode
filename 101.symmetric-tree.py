#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def in_order(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [root]
        return [root.val] + self.in_order(root.right) + self.in_order(root.left)

    def pre_order(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [root]
        return [root.val] + self.pre_order(root.left) + self.pre_order(root.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.pre_order(root.left) == self.in_order(root.right)


# @lc code=end

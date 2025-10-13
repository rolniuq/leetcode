#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        res = []

        if root.left:
            paths = self.binaryTreePaths(root.left)
            res += [str(root.val) + "->" + path for path in paths]

        if root.right:
            paths = self.binaryTreePaths(root.right)
            res += [str(root.val) + "->" + path for path in paths]

        return res


# @lc code=end

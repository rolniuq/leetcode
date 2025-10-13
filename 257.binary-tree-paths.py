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

        res = []
        if not root.left and not root.right:
            return res
        elif not root.left:
            return self.binaryTreePaths(root.right)
        elif not root.right:
            return self.binaryTreePaths(root.left)

        res.append(root.val)

        return [self.binaryTreePaths(root.left), self.binaryTreePaths(root.right)]


# @lc code=end

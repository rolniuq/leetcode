#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def LNR(self, root: Optional[TreeNode], arr: List[int]):
        if not root:
            return
        self.LNR(root.left, arr)
        arr.append(root.val)
        self.LNR(root.right, arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.LNR(root, res)
        return res


# @lc code=end

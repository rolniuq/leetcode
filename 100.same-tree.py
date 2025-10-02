#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def list_nodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [root]
        return [root.val] + self.list_nodes(root.left) + self.list_nodes(root.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.list_nodes(q) == self.list_nodes(p)


# @lc code=end

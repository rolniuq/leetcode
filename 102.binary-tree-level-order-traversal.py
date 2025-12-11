#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (71.73%)
# Likes:    16742
# Dislikes: 362
# Total Accepted:    3.2M
# Total Submissions: 4.4M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
#
#
#
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree nodefrom typing import Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        res = [[root.val]]
        queue = [[root]]
        while len(queue) > 0:
            path, val = [], []
            nodes = queue.pop(0)
            for node in nodes:
                if node.left:
                    val.append(node.left.val)
                    path.append(node.left)
                if node.right:
                    val.append(node.right.val)
                    path.append(node.right)

            if len(path):
                queue.append(path)
            if len(val):
                res.append(val)

        return res


# @lc code=end

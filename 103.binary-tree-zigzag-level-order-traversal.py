#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (62.77%)
# Likes:    11833
# Dislikes: 344
# Total Accepted:    1.7M
# Total Submissions: 2.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
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
# -100 <= Node.val <= 100
#
#
#
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        res = [[root.val]]
        queue = [[root]]
        level = 0
        while len(queue) > 0:
            level += 1
            nodes = queue.pop(0)
            path, val = [], []

            for node in nodes:
                if node.right:
                    path.append(node.right)
                    val.append(node.right.val)
                if node.left:
                    path.append(node.left)
                    val.append(node.left.val)

            if level % 2 == 0:
                val.reverse()

            if len(path):
                queue.append(path)
            if len(val):
                res.append(val)

        return res


# @lc code=end

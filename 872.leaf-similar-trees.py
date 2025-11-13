#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (70.16%)
# Likes:    4327
# Dislikes: 123
# Total Accepted:    646.2K
# Total Submissions: 921.1K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' + '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree, from left to right order, the
# values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
#
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
#
#
# Example 1:
#
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
#
# Example 2:
#
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leafs(self, root: TreeNode, arr: List[int]):
        if not root:
            return

        if not root.left and not root.right:
            arr.append(root.val)
            return

        self.get_leafs(root.left, arr)
        self.get_leafs(root.right, arr)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1, arr2 = [], []
        self.get_leafs(root1, arr1)
        self.get_leafs(root2, arr2)

        if len(arr1) != len(arr2):
            return False

        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False

        return True


# @lc code=end

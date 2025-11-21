#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (53.72%)
# Likes:    10163
# Dislikes: 374
# Total Accepted:    789.1K
# Total Submissions: 1.5M
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
#
# Basically, the deletion can be divided into two stages:
#
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and
# delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's
# also accepted.
#
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
#
#
# Example 3:
#
#
# Input: root = [], key = 0
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# Each node has a unique value.
# root is a valid binary search tree.
# -10^5 <= key <= 10^5
#
#
#
# Follow up: Could you solve it with time complexity O(height of tree)?
#
#

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def generator(self, start: int, end: int) -> List[Optional[TreeNode]]:
        if start > end:
            return [None]

        res = []

        for i in range(start, end + 1):
            left_nodes = self.generator(start, i - 1)
            right_nodes = self.generator(i + 1, end)

            for left_node in left_nodes:
                for right_node in right_nodes:
                    node = TreeNode(i, left_node, right_node)
                    res.append(node)

        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        return self.generator(1, n)

    def in_order(self, root: Optional[TreeNode]):
        if root is None:
            print("None")
            return

        print(root.val)

        self.in_order(root.left)
        self.in_order(root.right)

    def build_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            # right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getNode(
        self, parent: Optional[TreeNode], node: Optional[TreeNode], key: int
    ) -> tuple[Optional[TreeNode], Optional[TreeNode]]:
        if node is None:
            return node, parent

        if node.val == key:
            return node, parent

        left_node, parent_left = self.getNode(node, node.left, key)
        if left_node:
            return left_node, parent_left

        return self.getNode(node, node.right, key)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        node, parent = self.getNode(None, root, key)
        if node:
            if not node.left and not node.right:
                if not parent:
                    return None

                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            elif node.left and not node.right:
                if not parent:
                    return node.left

                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
            elif not node.left and node.right:
                if not parent:
                    return node.right
                if parent.right == node:
                    parent.right = node.right
                else:
                    parent.left = node.right
            else:
                # find the smallest node in node.right
                parent_succ = node
                succ = node.right
                while succ.left:
                    parent_succ = succ
                    succ = succ.left

                node.val = succ.val
                if parent_succ.left == succ:
                    parent_succ.left = succ.right
                else:
                    parent_succ.right = succ.right

        return root


# @lc code=end
def run():
    bst = BST()
    # l = list([5, 3, 6, 2, 4, None, 7])
    # l = list([1, None, 2])
    l = list([0])
    root = bst.build_tree(l)

    s = Solution()
    res = s.deleteNode(root, 0)
    print("[SOLUTION]")
    bst.in_order(res)


run()

#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.

from typing import List, Optional


class Solution:
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


# @lc code=end
def printNode(node: TreeNode):
    if not node:
        return

    print("[DEBUG]", node.val)
    printNode(node.left)
    printNode(node.right)


def run():
    s = Solution()
    roots = s.generateTrees(3)
    for root in roots:
        printNode(root)
        print("=======")


run()

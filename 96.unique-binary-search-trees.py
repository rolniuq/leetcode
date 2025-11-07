#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (62.91%)
# Likes:    10873
# Dislikes: 439
# Total Accepted:    810.6K
# Total Submissions: 1.3M
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 19
#
#
#


# @lc code=start
class Solution:
    def traversal(self, n: int, memo: dict[int, int]) -> int:
        if n == 0:
            return 1

        if n in memo:
            return memo[n]

        count = 0

        # node must be from 1 to n
        for i in range(1, n + 1):
            left = self.traversal(i - 1, memo)
            right = self.traversal(n - i, memo)
            count += left * right

        memo[n] = count

        return memo[n]

    def numTrees(self, n: int) -> int:
        memo = {}
        return self.traversal(n, memo)


# @lc code=end


def run():
    s = Solution()
    print("[SOLUTION]:", s.numTrees(3))


run()

#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (67.30%)
# Likes:    13402
# Dislikes: 190
# Total Accepted:    1.7M
# Total Submissions: 2.5M
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#
# Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
#
#
#

from typing import List
import math


# @lc code=start
class Solution:
    def traversal(
        self,
        m: int,
        n: int,
        memo: dict[tuple[int, int], int],
        grid: List[List[int]],
    ) -> int:
        if m < 0 or n < 0:
            return math.inf

        if m == 0 and n == 0:
            return grid[0][0]

        if (m, n) in memo:
            return memo[m, n]

        memo[m, n] = grid[m][n] + min(
            self.traversal(m - 1, n, memo, grid),
            self.traversal(m, n - 1, memo, grid),
        )

        return memo[m, n]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}
        return self.traversal(m - 1, n - 1, memo, grid)


# @lc code=end
def run():
    s = Solution()
    grid = list(([1, 3, 1], [1, 5, 1], [4, 2, 1]))
    print("[SOLUTION]:", s.minPathSum(grid))


run()

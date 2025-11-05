#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (43.73%)
# Likes:    9482
# Dislikes: 553
# Total Accepted:    1.3M
# Total Submissions: 3.1M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# You are given an m x n integer array grid. There is a robot initially located
# at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that
# the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach
# the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to
# 2 * 10^9.
#
#
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
#
#
#

from typing import List


# @lc code=start
class Solution:
    def traversal(
        self, m: int, n: int, memo: dict[tuple[int, int], int], grid: List[List[int]]
    ) -> int:
        if m == 0 and n == 0 and grid[m][n] == 0:
            return 1

        if m < 0 or n < 0 or grid[m][n] == 1:
            return 0

        if (m, n) in memo:
            return memo[(m, n)]

        memo[m, n] = self.traversal(m - 1, n, memo, grid) + self.traversal(
            m, n - 1, memo, grid
        )

        return memo[m, n]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}

        if obstacleGrid[0][0] == 1:
            return 0

        return self.traversal(m - 1, n - 1, memo, obstacleGrid)


# @lc code=end


def run():
    s = Solution()

    l = list(
        (
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ),
    )  # 2

    # l = list(
    #     ([0, 1], [0, 0]),
    # )  # 1

    # l = list(
    #     ([[1, 0]]),
    # ) # 0

    print("[SOLUTION]:", s.uniquePathsWithObstacles(l))


run()

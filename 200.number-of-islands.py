#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (63.39%)
# Likes:    24527
# Dislikes: 600
# Total Accepted:    3.8M
# Total Submissions: 6.1M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def bfs(self, grid: List[List[str]], n: int, d: int, c: int, r: int):
        queue = [(c, r)]
        grid[c][r] = "0"

        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx = dx + x
                nd = dy + y
                if 0 <= nx < n and 0 <= nd < d and grid[nx][nd] == "1":
                    grid[nx][nd] = "0"
                    queue.append((nx, nd))

    def numIslands(self, grid: List[List[str]]) -> int:
        isLands = 0
        n, d = len(grid), len(grid[0])
        for i in range(n):
            for j in range(d):
                if grid[i][j] == "1":
                    isLands += 1
                    self.bfs(grid, n, d, i, j)

        return isLands


# @lc code=end

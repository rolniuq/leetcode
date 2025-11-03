#
# @lc app=leetcode id=2257 lang=python3
#
# [2257] Count Unguarded Cells in the Grid
#
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/
#
# algorithms
# Medium (65.67%)
# Likes:    932
# Dislikes: 78
# Total Accepted:    112.3K
# Total Submissions: 170.6K
# Testcase Example:  '4\n6\n[[0,0],[1,1],[2,3]]\n[[0,1],[2,2],[1,4]]'
#
# You are given two integers m and n representing a 0-indexed m x n grid. You
# are also given two 2D integer arrays guards and walls where guards[i] =
# [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the i^th
# guard and j^th wall respectively.
#
# A guard can see every cell in the four cardinal directions (north, east,
# south, or west) starting from their position unless obstructed by a wall or
# another guard. A cell is guarded if there is at least one guard that can see
# it.
#
# Return the number of unoccupied cells that are not guarded.
#
#
# Example 1:
#
#
# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls =
# [[0,1],[2,2],[1,4]]
# Output: 7
# Explanation: The guarded and unguarded cells are shown in red and green
# respectively in the above diagram.
# There are a total of 7 unguarded cells, so we return 7.
#
#
# Example 2:
#
#
# Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
# Output: 4
# Explanation: The unguarded cells are shown in green in the above diagram.
# There are a total of 4 unguarded cells, so we return 4.
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 10^5
# 2 <= m * n <= 10^5
# 1 <= guards.length, walls.length <= 5 * 10^4
# 2 <= guards.length + walls.length <= m * n
# guards[i].length == walls[j].length == 2
# 0 <= rowi, rowj < m
# 0 <= coli, colj < n
# All the positions in guards and walls are unique.
#
#
#

from typing import List


# @lc code=start
class Solution:
    # 0: unguarded
    # 1: guarded
    # 2: guard pos || wall pos
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = []
        for _ in range(m):
            grid.append([0] * n)

        for row, col in guards:
            grid[row][col] = 2

        for row, col in walls:
            grid[row][col] = 2

        directors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for guard_row, guard_col in guards:
            for director_row, director_col in directors:
                cur_row, cur_col = guard_row, guard_col

                while (
                    0 <= cur_row + director_row < m
                    and 0 <= cur_col + director_col < n
                    and grid[cur_row + director_row][cur_col + director_col] != 2
                ):
                    cur_row += director_row
                    cur_col += director_col
                    grid[cur_row][cur_col] = 1

        return sum(cell == 0 for row in grid for cell in row)


# @lc code=end


def run():
    s = Solution()
    print(
        "[SOLUTION]:",
        s.countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]),
    )


run()

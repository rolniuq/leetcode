/*
 * @lc app=leetcode id=2257 lang=golang
 *
 * [2257] Count Unguarded Cells in the Grid
 *
 * https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/
 *
 * algorithms
 * Medium (65.67%)
 * Likes:    932
 * Dislikes: 78
 * Total Accepted:    112.3K
 * Total Submissions: 170.6K
 * Testcase Example:  '4\n6\n[[0,0],[1,1],[2,3]]\n[[0,1],[2,2],[1,4]]'
 *
 * You are given two integers m and n representing a 0-indexed m x n grid. You
 * are also given two 2D integer arrays guards and walls where guards[i] =
 * [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the i^th
 * guard and j^th wall respectively.
 *
 * A guard can see every cell in the four cardinal directions (north, east,
 * south, or west) starting from their position unless obstructed by a wall or
 * another guard. A cell is guarded if there is at least one guard that can see
 * it.
 *
 * Return the number of unoccupied cells that are not guarded.
 *
 *
 * Example 1:
 *
 *
 * Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls =
 * [[0,1],[2,2],[1,4]]
 * Output: 7
 * Explanation: The guarded and unguarded cells are shown in red and green
 * respectively in the above diagram.
 * There are a total of 7 unguarded cells, so we return 7.
 *
 *
 * Example 2:
 *
 *
 * Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
 * Output: 4
 * Explanation: The unguarded cells are shown in green in the above diagram.
 * There are a total of 4 unguarded cells, so we return 4.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= m, n <= 10^5
 * 2 <= m * n <= 10^5
 * 1 <= guards.length, walls.length <= 5 * 10^4
 * 2 <= guards.length + walls.length <= m * n
 * guards[i].length == walls[j].length == 2
 * 0 <= rowi, rowj < m
 * 0 <= coli, colj < n
 * All the positions in guards and walls are unique.
 *
 *
 */

package leetcode

// @lc code=start

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	grid := make([][]int, 0)
	for range m {
		row := make([]int, n)
		grid = append(grid, row)
	}

	for _, pos := range guards {
		grid[pos[0]][pos[1]] = 2
	}

	for _, pos := range walls {
		grid[pos[0]][pos[1]] = 2
	}

	directors := [][]int{{-1, 0}, {0, -1}, {1, 0}, {0, 1}}
	for _, g_pos := range guards {
		g_row, g_col := g_pos[0], g_pos[1]

		for _, d_pos := range directors {
			d_row, d_col := d_pos[0], d_pos[1]

			cur_row := g_row
			cur_col := g_col

			for 0 <= d_row+cur_row && d_row+cur_row < m &&
				0 <= d_col+cur_col && d_col+cur_col < n &&
				grid[d_row+cur_row][d_col+cur_col] != 2 {
				cur_row += d_row
				cur_col += d_col
				grid[cur_row][cur_col] = 1
			}
		}
	}

	res := 0

	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == 0 {
				res += 1
			}
		}
	}

	return res
}

// @lc code=end

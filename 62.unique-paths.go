/*
 * @lc app=leetcode id=62 lang=golang
 *
 * [62] Unique Paths
 *
 * https://leetcode.com/problems/unique-paths/description/
 *
 * algorithms
 * Medium (66.22%)
 * Likes:    17982
 * Dislikes: 485
 * Total Accepted:    2.6M
 * Total Submissions: 3.9M
 * Testcase Example:  '3\n7'
 *
 * There is a robot on an m x n grid. The robot is initially located at the
 * top-left corner (i.e., grid[0][0]). The robot tries to move to the
 * bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
 * either down or right at any point in time.
 *
 * Given the two integers m and n, return the number of possible unique paths
 * that the robot can take to reach the bottom-right corner.
 *
 * The test cases are generated so that the answer will be less than or equal
 * to 2 * 10^9.
 *
 *
 * Example 1:
 *
 *
 * Input: m = 3, n = 7
 * Output: 28
 *
 *
 * Example 2:
 *
 *
 * Input: m = 3, n = 2
 * Output: 3
 * Explanation: From the top-left corner, there are a total of 3 ways to reach
 * the bottom-right corner:
 * 1. Right -> Down -> Down
 * 2. Down -> Down -> Right
 * 3. Down -> Right -> Down
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= m, n <= 100
 *
 *
 */
package leetcode

// @lc code=start
type Unique struct {
	First int
	Last  int
}

func traversal(m, n int, memo map[Unique]int) int {
	if val, ok := memo[Unique{First: m, Last: n}]; ok {
		return val
	}

	if m == 1 || n == 1 {
		return 1
	}

	memo[Unique{First: m, Last: n}] = traversal(m-1, n, memo) + traversal(m, n-1, memo)

	return memo[Unique{First: m, Last: n}]
}

func uniquePaths(m int, n int) int {
	memo := make(map[Unique]int)

	return traversal(m, n, memo)
}

// @lc code=end

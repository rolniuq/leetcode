/*
 * @lc app=leetcode id=70 lang=golang
 *
 * [70] Climbing Stairs
 *
 * https://leetcode.com/problems/climbing-stairs/description/
 *
 * algorithms
 * Easy (53.74%)
 * Likes:    23871
 * Dislikes: 997
 * Total Accepted:    4.7M
 * Total Submissions: 8.7M
 * Testcase Example:  '2'
 *
 * You are climbing a staircase. It takes n steps to reach the top.
 *
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can
 * you climb to the top?
 *
 *
 * Example 1:
 *
 *
 * Input: n = 2
 * Output: 2
 * Explanation: There are two ways to climb to the top.
 * 1. 1 step + 1 step
 * 2. 2 steps
 *
 *
 * Example 2:
 *
 *
 * Input: n = 3
 * Output: 3
 * Explanation: There are three ways to climb to the top.
 * 1. 1 step + 1 step + 1 step
 * 2. 1 step + 2 steps
 * 3. 2 steps + 1 step
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 45
 *
 *
 */
package leetcode

// @lc code=start

func climb(n int, memo map[int]int) int {
	if n <= 2 {
		return n
	}

	if val, ok := memo[n]; ok {
		return val
	}

	memo[n] = climb(n-1, memo) + climb(n-2, memo)

	return memo[n]
}

func climbStairs(n int) int {
	memo := make(map[int]int, 0)
	return climb(n, memo)
}

// @lc code=end

/*
 * @lc app=leetcode id=22 lang=golang
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (77.85%)
 * Likes:    22832
 * Dislikes: 1063
 * Total Accepted:    2.6M
 * Total Submissions: 3.4M
 * Testcase Example:  '3'
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 *
 *
 * Example 1:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 * Example 2:
 * Input: n = 1
 * Output: ["()"]
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 8
 *
 *
 */
package leetcode

// @lc code=start
func generate(open, close, end int, path *[]byte, res *[]string) {
	if open == end && close == end {
		*res = append(*res, string(*path))
		return
	}

	if open < end {
		b := []byte("(")
		*path = append(*path, b...)
		generate(open+1, close, end, path, res)
		pVal := *path
		*path = pVal[:len(pVal)-1]
	}

	if close < open {
		b := []byte(")")
		*path = append(*path, b...)
		generate(open, close+1, end, path, res)
		pVal := *path
		*path = pVal[:len(pVal)-1]
	}
}

func generateParenthesis(n int) []string {
	res := []string{}
	path := []byte{}

	generate(0, 0, n, &path, &res)

	return res
}

// @lc code=end

/*
 * @lc app=leetcode id=77 lang=golang
 *
 * [77] Combinations
 *
 * https://leetcode.com/problems/combinations/description/
 *
 * algorithms
 * Medium (73.69%)
 * Likes:    8777
 * Dislikes: 246
 * Total Accepted:    1.2M
 * Total Submissions: 1.7M
 * Testcase Example:  '4\n2'
 *
 * Given two integers n and k, return all possible combinations of k numbers
 * chosen from the range [1, n].
 *
 * You may return the answer in any order.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 4, k = 2
 * Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
 * Explanation: There are 4 choose 2 = 6 total combinations.
 * Note that combinations are unordered, i.e., [1,2] and [2,1] are considered
 * to be the same combination.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 1, k = 1
 * Output: [[1]]
 * Explanation: There is 1 choose 1 = 1 total combination.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 20
 * 1 <= k <= n
 *
 *
 */
package leetcode

// @lc code=start

func combine(n int, k int) [][]int {
	var fn func(index, n, k int, path *[]int, res *[][]int)

	fn = func(index, n, k int, path *[]int, res *[][]int) {
		if k == len(*path) {
			tmp := make([]int, len(*path))
			copy(tmp, *path)
			*res = append(*res, tmp)
			return
		}

		if index > n {
			return
		}

		for i := index; i <= n; i++ {
			*path = append(*path, i)
			fn(i+1, n, k, path, res)
			pVal := *path
			*path = pVal[:len(pVal)-1]
		}
	}

	res := make([][]int, 0)
	path := make([]int, 0)
	fn(1, n, k, &path, &res)
	return res
}

// @lc code=end

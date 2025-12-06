/*
 * @lc app=leetcode id=40 lang=golang
 *
 * [40] Combination Sum II
 *
 * https://leetcode.com/problems/combination-sum-ii/description/
 *
 * algorithms
 * Medium (58.55%)
 * Likes:    12005
 * Dislikes: 374
 * Total Accepted:    1.6M
 * Total Submissions: 2.7M
 * Testcase Example:  '[10,1,2,7,6,1,5]\n8'
 *
 * Given a collection of candidate numbers (candidates) and a target number
 * (target), find all unique combinations in candidates where the candidate
 * numbers sum to target.
 *
 * Each number in candidates may only be used once in the combination.
 *
 * Note: The solution set must not contain duplicate combinations.
 *
 *
 * Example 1:
 *
 *
 * Input: candidates = [10,1,2,7,6,1,5], target = 8
 * Output:
 * [
 * [1,1,6],
 * [1,2,5],
 * [1,7],
 * [2,6]
 * ]
 *
 *
 * Example 2:
 *
 *
 * Input: candidates = [2,5,2,1,2], target = 5
 * Output:
 * [
 * [1,2,2],
 * [5]
 * ]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= candidates.length <= 100
 * 1 <= candidates[i] <= 50
 * 1 <= target <= 30
 *
 *
 */
package leetcode

import "sort"

// @lc code=start
func combineSum2(index int, path *[]int, res *[][]int, candidates []int, target int, cur int) {
	if cur == target {
		temp := make([]int, len(*path))
		copy(temp, *path)
		*res = append(*res, temp)
		return
	}

	if cur > target || index >= len(candidates) {
		return
	}

	for i := index; i < len(candidates); i++ {
		if i > index && candidates[i] == candidates[i-1] {
			continue
		}

		*path = append(*path, candidates[i])
		combineSum2(i+1, path, res, candidates, target, cur+candidates[i])
		vPath := *path
		*path = vPath[:len(vPath)-1]
	}
}

func combinationSum2(candidates []int, target int) [][]int {
	res := make([][]int, 0)
	path := make([]int, 0)
	sort.Ints(candidates)
	combineSum2(0, &path, &res, candidates, target, 0)

	return res
}

// @lc code=end

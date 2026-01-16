/*
 * @lc app=leetcode id=11 lang=golang
 *
 * [11] Container With Most Water
 *
 * https://leetcode.com/problems/container-with-most-water/description/
 *
 * algorithms
 * Medium (59.23%)
 * Likes:    33441
 * Dislikes: 2149
 * Total Accepted:    4.9M
 * Total Submissions: 8.3M
 * Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
 *
 * You are given an integer array height of length n. There are n vertical
 * lines drawn such that the two endpoints of the i^th line are (i, 0) and (i,
 * height[i]).
 *
 * Find two lines that together with the x-axis form a container, such that the
 * container contains the most water.
 *
 * Return the maximum amount of water a container can store.
 *
 * Notice that you may not slant the container.
 *
 *
 * Example 1:
 *
 *
 * Input: height = [1,8,6,2,5,4,8,3,7]
 * Output: 49
 * Explanation: The above vertical lines are represented by array
 * [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
 * container can contain is 49.
 *
 *
 * Example 2:
 *
 *
 * Input: height = [1,1]
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * n == height.length
 * 2 <= n <= 10^5
 * 0 <= height[i] <= 10^4
 *
 *
 */

package lc

import "math"

// @lc code=start

func maxArea(height []int) int {
	max := 0
	left, right := 0, len(height)-1
	for left < right {
		d := float64(right - left)
		c := math.Min(float64(height[left]), float64(height[right]))
		max = int(math.Max(float64(max), d*c))
		if height[left] > height[right] {
			right--
		} else {
			left++
		}
	}

	return max
}

// @lc code=end

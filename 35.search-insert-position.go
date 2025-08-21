package leetcode

/*
 * @lc app=leetcode id=35 lang=golang
 *
 * [35] Search Insert Position
 */

// @lc code=start
func searchInsert(nums []int, target int) int {
	if len(nums) == 0 {
		return 0
	}

	if nums[len(nums)-1] < target {
		return len(nums)
	}

	position := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] >= target {
			position = i
			break
		}
	}

	return position
}

// @lc code=end

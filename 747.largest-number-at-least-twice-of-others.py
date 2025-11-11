#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (51.49%)
# Likes:    1331
# Dislikes: 947
# Total Accepted:    316.3K
# Total Submissions: 613.8K
# Testcase Example:  '[3,6,1,0]'
#
# You are given an integer array nums where the largest integer is unique.
#
# Determine whether the largest element in the array is at least twice as much
# as every other number in the array. If it is, return the index of the largest
# element, or return -1 otherwise.
#
#
# Example 1:
#
#
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.
#
#
#

from typing import List
import math


# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        index = -1
        first, second = -math.inf, -math.inf
        for i in range(len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
                index = i
            elif nums[i] > second:
                second = nums[i]

        return index if second * 2 <= first else -1


# @lc code=end
def run():
    s = Solution()
    l = list([3, 6, 1, 0])  # 1
    # l = list([1, 2, 3, 4])  # -1
    # l = list([0, 0, 0, 1])  # 3
    # l = list([0, 0, 1, 0])  # 2
    print("[SOLUTION]:", s.dominantIndex(l))


run()

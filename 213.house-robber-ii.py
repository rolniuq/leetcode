#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (44.19%)
# Likes:    10807
# Dislikes: 181
# Total Accepted:    1.1M
# Total Submissions: 2.6M
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2), because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
#
#
#

from typing import List


# @lc code=start
class Solution:
    def robber(
        self, start: int, end: int, nums: List[int], memo: dict[int, int]
    ) -> int:
        if start >= end:
            return 0

        if start in memo:
            return memo[start]

        memo[start] = max(
            nums[start] + self.robber(start + 2, end, nums, memo),
            self.robber(start + 1, end, nums, memo),
        )

        return memo[start]

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        memo1, memo2 = {}, {}
        return max(
            self.robber(0, len(nums) - 1, nums, memo1),
            self.robber(1, len(nums), nums, memo2),
        )


# @lc code=end
def run():
    s = Solution()
    # l = list([1, 2, 3, 1])  # 4
    # l = list([2, 3, 2])  # 3
    l = list([1, 2, 3])  # 3
    print("[SOLUTION]:", s.rob(l))


run()

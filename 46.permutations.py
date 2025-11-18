#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (81.25%)
# Likes:    20501
# Dislikes: 373
# Total Accepted:    2.9M
# Total Submissions: 3.5M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def back_tracking(
        self,
        index: int,
        res: List[List[int]],
        nums: List[int],
    ):
        if index == len(nums):
            res.append(nums.copy())
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.back_tracking(index + 1, res, nums)
            nums[index], nums[i] = nums[i], nums[index]

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.back_tracking(0, res, nums)
        return res


# @lc code=end


def run():
    s = Solution()
    l = list([1, 2, 3])
    print("[SOLUTION]:", s.permute(l))


run()

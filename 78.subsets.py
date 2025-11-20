#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (81.61%)
# Likes:    18801
# Dislikes: 333
# Total Accepted:    2.8M
# Total Submissions: 3.4M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#

from typing import List


# @lc code=start
class Solution:
    def backTracking(
        self, index: int, path: List[int], res: List[List[int]], nums: List[int]
    ):
        if index == len(nums):
            res.append(path.copy())
            return

        self.backTracking(index + 1, path, res, nums)

        path.append(nums[index])
        self.backTracking(index + 1, path, res, nums)
        path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        self.backTracking(0, path, res, nums)
        return res


# @lc code=end


def run():
    s = Solution()
    l = list([1, 2, 3])
    print("[SOLUTION]:", s.subsets(l))


run()

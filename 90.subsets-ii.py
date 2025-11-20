#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (60.34%)
# Likes:    10684
# Dislikes: 395
# Total Accepted:    1.4M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
#
#
from typing import List


# @lc code=start
class Solution:
    def stupid_backTracking(
        self,
        index: int,
        path: List[int],
        res: List[List[int]],
        nums: List[int],
    ):
        if index == len(nums):
            res.append(path.copy())
            return

        self.stupid_backTracking(index + 1, path, res, nums)

        path.append(nums[index])
        self.stupid_backTracking(index + 1, path, res, nums)
        path.pop()

    def backTracking(
        self, index: int, path: List[int], res: List[List[int]], nums: List[int]
    ):
        res.append(path.copy())

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            self.backTracking(i + 1, path, res, nums)
            path.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        nums.sort()
        # self.stupid_backTracking(0, path, res, nums)
        self.backTracking(0, path, res, nums)
        return res


# @lc code=end
def run():
    s = Solution()
    l = list([1, 2, 2])  # [[],[1],[1,2],[1,2,2],[2],[2,2]
    print("[SOLUTION]:", s.subsetsWithDup(l))


run()

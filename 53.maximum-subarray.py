#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
from typing import List
import math


class Solution:
    def maxSubArrayExceed(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        curSum = -math.inf
        maxSum = curSum

        for i in range(0, len(nums)):
            curSum = nums[i]

            if curSum > maxSum:
                maxSum = curSum

            if i == len(nums) - 1:
                break

            for j in range(i + 1, len(nums)):
                curSum += nums[j]
                if curSum > maxSum:
                    maxSum = curSum

        return maxSum

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)

        return maxSum


def run():
    s = Solution()
    print("[SOLUTION]:", s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("[SOLUTION]: ", s.maxSubArray([5, 4, -1, 7, 8]))
    print("[SOLUTION]: ", s.maxSubArray([-2, 1]))  # 1
    print("[SOLUTION]: ", s.maxSubArray([-2, -1]))  # -1
    print("[SOLUTION]: ", s.maxSubArray([-1, -2]))  # - 1


run()


# @lc code=end

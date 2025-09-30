#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc code=start
import math


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = math.inf
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(closest_sum - target):
                    closest_sum = sum
                if sum > target:
                    right -= 1
                else:
                    left += 1

        return closest_sum


def run():
    s = Solution()
    print("[INFO]", s.threeSumClosest([-1, 2, 1, 4], 1))


run()


# @lc code=end

#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        counter = 0
        while counter < len(nums):
            if nums[counter] == target:
                if ans[0] == -1:
                    ans[0] = counter
                    ans[1] = counter
                else:
                    ans[1] = counter

            counter += 1

        return ans

    def bisect_left(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.bisect_left(nums, target), self.bisect_left(nums, target + 1)
        if left == right:
            return [-1, -1]

        return [left, right - 1]


def run():
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))


run()


# @lc code=end

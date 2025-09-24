#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#


# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        counter = dict()
        n = len(nums) // 2
        while left <= right:
            counter[nums[left]] = counter.get(nums[left], 0) + 1
            counter[nums[right]] = counter.get(nums[right], 0) + 1

            if counter[nums[left]] == n:
                return nums[left]
            if counter[nums[right]] == n:
                return nums[right]

            left += 1
            right -= 1

        return 0


# @lc code=end

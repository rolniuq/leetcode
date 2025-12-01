#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

from typing import List


# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        next_even = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[next_even], nums[i] = nums[i], nums[next_even]
                next_even += 1

        return nums


# @lc code=end
def run():
    s = Solution()
    l = list([3, 1, 2, 4])
    print("[SOLUTION]:", s.sortArrayByParity(l))


run()

#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
import math

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first_max = second_max = third_max = -math.inf

        for n in nums:
            if n > first_max:
                third_max = second_max
                second_max = first_max
                first_max = n
            elif n < first_max and n > second_max:
                third_max = second_max
                second_max = n
            elif n > third_max and n < second_max:
                third_max = n

        if third_max != -math.inf and third_max != second_max:
            return int(third_max)

        return int(first_max)
# @lc code=end


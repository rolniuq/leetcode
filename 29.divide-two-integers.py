#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (divisor < 0) ^ (dividend < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        if divisor == 1:
            if is_negative:
                return -dividend
            else:
                if dividend >= 2**31:
                    dividend = 2**31 - 1

                return dividend

        left, right = 0, dividend
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * divisor <= dividend:
                left = mid + 1
            else:
                right = mid - 1

        return -(right) if is_negative else right


# @lc code=end

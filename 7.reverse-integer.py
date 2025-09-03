#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        saver = x
        if saver < 0:
            saver = abs(saver)

        original = 0
        while saver > 0:
            digit = saver % 10
            original = original * 10 + digit
            saver //= 10

        if x < 0:
            original = -original

        return original if -2**31 <= original <= 2**31 - 1 else 0
# @lc code=end


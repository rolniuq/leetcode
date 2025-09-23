#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#


# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return True

        for i in range(1, num // 2 + 5):
            if i * i - num > 0:
                return False
            elif i * i - num == 0:
                return True

        return False


# @lc code=end

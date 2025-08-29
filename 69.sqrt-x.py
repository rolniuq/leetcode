#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        for i in range(1, x//2 + 5):
            if i * i - x > 0:
                return i - 1
            elif i * i -x == 0:
                return i

        return 1

# @lc code=end


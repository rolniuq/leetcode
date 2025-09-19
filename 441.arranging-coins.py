#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#


# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1:
            return n

        counter = 1
        while n > 0:
            n -= counter
            if n < 0:
                return counter - 1

            counter += 1

        return counter - 1


# @lc code=end

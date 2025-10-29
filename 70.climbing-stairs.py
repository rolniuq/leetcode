#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climb(self, n: int, memo: dict[int, int]) -> int:
        if n in memo:
            return memo[n]

        if n <= 2:
            return n

        memo[n] = self.climb(n - 1, memo) + self.climb(n - 2, memo)

        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climb(n, memo)


# @lc code=end

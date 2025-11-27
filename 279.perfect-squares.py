#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

import math
from typing import List


# @lc code=start
class Solution:
    def __init__(self):
        self.perfect = []
        pass

    def dp(self, amount: int, memo: dict[int, int]) -> int:
        if amount < 0:
            return math.inf

        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        best = math.inf
        for p in self.perfect:
            best = min(best, self.dp(amount - p, memo) + 1)

        memo[amount] = best

        return memo[amount]

    def backTracking(self, index: int, n: int, count: int):
        if n < 0 or index < 0:
            return

        if n == 0:
            self.min_count = min(self.min_count, count)
            return

        self.backTracking(index, n - self.perfect[index], count + 1)
        self.backTracking(index - 1, n, count)

    def numSquares(self, n: int) -> int:
        self.perfect = [i * i for i in range(1, int(n**0.5) + 1)]

        memo = {}
        return self.dp(n, memo)

        # self.min_count = float("inf")
        # self.backTracking(len(self.perfect) - 1, n, 0)
        # return self.min_count if self.min_count != math.inf else 0


# @lc code=end


def run():
    s = Solution()
    tests = [12]

    for n in tests:
        print(f"[SOLUTION]: with: {n} we got {s.numSquares(n)}")


run()

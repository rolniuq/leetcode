#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

from typing import List
import math


# @lc code=start
class Solution:
    def count(self, coins: List[int], amount: int, memo: dict[int, int]) -> int:
        if amount < 0:
            return math.inf
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]

        best = math.inf
        for c in coins:
            best = min(best, self.count(coins, amount - c, memo) + 1)

        memo[amount] = best

        return memo[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        ans = self.count(coins, amount, memo)
        return ans if ans != math.inf else -1


# @lc code=end


def run():
    s = Solution()
    tests = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
    ]

    for coins, target in tests:
        print(f"coins={coins}, target={target} -> {s.coinChange(coins, target)}")


run()

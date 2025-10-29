#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:
    def traversal(self, m: int, n: int, memo: dict[tuple[int, int], int]) -> int:
        if m == 1 or n == 1:
            return 1

        if (m, n) in memo:
            return memo[(m, n)]

        memo[(m, n)] = self.traversal(m - 1, n, memo) + self.traversal(m, n - 1, memo)

        return memo[(m, n)]

    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.traversal(m, n, memo)


# @lc code=end

#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
# https://leetcode.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (63.43%)
# Likes:    4735
# Dislikes: 208
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '4'
#
# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
#
# Example 2:
#
#
# Input: n = 25
# Output: 1389537
#
#
#
# Constraints:
#
#
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 -
# 1.
#
#
#


# @lc code=start
class Solution:
    def tribonacci_with_memo(self, n: int, memo: dict[int, int]) -> int:
        if n in memo:
            return memo[n]

        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        memo[n] = (
            self.tribonacci_with_memo(n - 3, memo)
            + self.tribonacci_with_memo(n - 2, memo)
            + self.tribonacci_with_memo(n - 1, memo)
        )

        return memo[n]

    def tribonacci(self, n: int) -> int:
        memo = {}
        return self.tribonacci_with_memo(n, memo)


def run():
    s = Solution()
    # 0 1 1 2 4
    print("[SOLUTION]", s.tribonacci(3))
    print("[SOLUTION]", s.tribonacci(5))
    print("[SOLUTION]", s.tribonacci(4))  # 4


run()


# @lc code=end

#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (80.14%)
# Likes:    11735
# Dislikes: 598
# Total Accepted:    1.5M
# Total Submissions: 1.9M
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
#
# Example 2:
#
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^5
#
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
#
#
#

from typing import List


# @lc code=start
class Solution:
    def binary(self, n: int) -> List[int]:
        res = []
        while n > 0:
            res.insert(0, n % 2)
            n = n // 2

        return res

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            arr = self.binary(i)
            res.append(sum(item == 1 for item in arr))

        return res

    def countBitsDP(self, n: int) -> List[int]:
        # dp[i] = dp[i//2] + (i%2)

        # if i is odd -> mid = length//2 and move 1 bit left: 13/2 = 6 <=> 1101 = 13, 110 = 6 -> move 1 bit left -> 110 1 = 13
        # if i is event -> mid = length//2 and move 1 bit left: 12/2 = 6 <=> 1100 = 12, 110 = 6 0> move 1 bit left -> 110 0 = 12
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i // 2] + (i % 2)
        return res


# @lc code=end


def run():
    s = Solution()
    print("[DEBUG]: ", s.countBitsDP(2))
    print("[DEBUG]: ", s.countBitsDP(5))


run()

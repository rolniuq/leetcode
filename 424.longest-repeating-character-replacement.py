#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#


# @lc code=start
import math


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        d = dict()
        max_freq = 0

        for right in range(len(s)):
            d[s[right]] = d.get(s[right], 0) + 1
            max_freq = max(max_freq, d[s[right]])
            while (right - left + 1) - max_freq > k:
                d[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len


def run():
    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s, k))


run()


# @lc code=end

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
        arr = [s[left]]
        h = k

        for right in range(1, len(s)):
            if h >= 0:
                arr.append(s[right])
            else:
                max_len = max(max_len, len(arr))
                left += 1
                arr = [s[left]]
                h = k

            if s[right] not in arr:
                h -= 1

        return max_len


def run():
    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s, k))


run()


# @lc code=end

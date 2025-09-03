#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = s[0]

        for i in range(len(s)):
            left = i
            right = i + 1
            while right < len(s):
                if self.isPalindrome(s[left:right + 1]):
                    if right - left + 1 > max_len:
                        max_len = right - left + 1
                        res = s[left:right + 1]
                right += 1


        return res
# @lc code=end


#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        for char in s:
            if dict.get(char) is None:
                dict[char] = 1
            else:
                dict[char] += 1

        even_counter = 0
        for v in dict.values():
            if v % 2 == 0:
                even_counter += v
            else:
                even_counter += v - 1

        if even_counter < len(s):
            return even_counter + 1

        return even_counter


# @lc code=end

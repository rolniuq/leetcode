#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (48.04%)
# Likes:    12723
# Dislikes: 513
# Total Accepted:    1.4M
# Total Submissions: 2.8M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of
# s2.
#
#
# Example 1:
#
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
# Example 2:
#
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
#
#
#
from collections import Counter


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        if s1 == s2:
            return True

        s1_count = Counter(s1)
        window_count = Counter()
        left = 0
        for right in range(len(s2)):
            window_count[s2[right]] += 1

            # thu nhỏ bên trái
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1

            if window_count == s1_count:
                return True

        return False


# @lc code=end
def run():
    s = Solution()
    # print("[SOLUTION]:", s.checkInclusion("ab", "eidbaooo"))
    # print("[SOLUTION]:", s.checkInclusion("ab", "ab"))
    print("[SOLUTION]:", s.checkInclusion("abc", "bbbca"))
    # print("[SOLUTION]:", s.checkInclusion("a", "ab"))


run()

#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#
# https://leetcode.com/problems/most-common-word/description/
#
# algorithms
# Easy (44.85%)
# Likes:    1821
# Dislikes: 3111
# Total Accepted:    435.9K
# Total Submissions: 971.5K
# Testcase Example:  '"Bob hit a ball, the hit BALL flew far after it was hit."\n["hit"]'
#
# Given a string paragraph and a string array of the banned words banned,
# return the most frequent word that is not banned. It is guaranteed there is
# at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned
# in lowercase.
#
# Note that words can not contain punctuation symbols.
#
#
# Example 1:
#
#
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent
# non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is
# banned.
#
#
# Example 2:
#
#
# Input: paragraph = "a.", banned = []
# Output: "a"
#
#
#
# Constraints:
#
#
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols:
# "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dp = {}
        for k in "!?',;.":
            paragraph = paragraph.replace(k, " ")

        words = paragraph.lower().split()
        for word in words:
            if word in banned:
                continue

            dp[word] = dp.get(word, 0) + 1

        max_val = 0
        max_ch = ""
        for k in dp:
            if dp[k] > max_val:
                max_val = dp[k]
                max_ch = k

        return max_ch


# @lc code=end
def run():
    s = Solution()
    str = "a b.b"
    print(s.mostCommonWord(str, []))


run()

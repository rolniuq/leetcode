#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (58.63%)
# Likes:    14779
# Dislikes: 238
# Total Accepted:    1.7M
# Total Submissions: 2.9M
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
# A common subsequence of two strings is a subsequence that is common to both
# strings.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
#
#
#


# @lc code=start
class Solution:
    def dp(
        self, i: int, j: int, text1: str, text2: str, memo: dict[tuple[int, int], int]
    ) -> int:
        if i == len(text1) + 1 or j == len(text2) + 1:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]
        if text1[i - 1] == text2[j - 1]:
            memo[(i, j)] = self.dp(i + 1, j + 1, text1, text2, memo) + 1
        else:
            memo[(i, j)] = max(
                self.dp(i + 1, j, text1, text2, memo),
                self.dp(i, j + 1, text1, text2, memo),
            )

        return memo[i, j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.dp(1, 1, text1, text2, memo)

        # n = len(text1)
        # m = len(text2)
        # dp = [[0] * (m + 1) for _ in range(n + 1)]

        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         if text1[i - 1] == text2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # return dp[n][m]


# @lc code=end
def run():
    s = Solution()
    print("[SOLUTION]:", s.longestCommonSubsequence("abcde", "ace"))


run()

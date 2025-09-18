#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
# abcabcbb 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        arr = []
        start, end, max_len = 0, 0, 0
        while end < len(s):
            if s[end] not in arr:
                arr.append(s[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
                arr.remove(s[start])
                start += 1

        return max_len


# @lc code=end


def run():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    # print(sol.lengthOfLongestSubstring("bbbbb"))
    # print(sol.lengthOfLongestSubstring("pwwkew"))


run()

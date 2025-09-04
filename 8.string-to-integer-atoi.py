#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        isNegative = False
        if s[0] == '-':
            isNegative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        elif not s[0].isdigit():
            return 0

        res = 0

        for char in s:
            if char.isdigit():
                res = res * 10 + int(char)
            else:
                break


        if res > 2**31 - 1:
            return -2**31 if isNegative else 2**31 - 1

        return res if not isNegative else -res
# @lc code=end


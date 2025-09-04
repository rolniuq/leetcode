#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a, b = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""

        while a >= 0 or b >= 0 or carry:
            x = int(num1[a]) if a >= 0 else 0
            y = int(num2[b]) if b >= 0 else 0

            total = x + y + carry
            carry = total // 10
            res += str(total % 10)
            a -= 1
            b -= 1

        return res[::-1]
# @lc code=end


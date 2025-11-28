#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#


# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        count = 10
        current_digits = 9
        unique_digits = 9

        for _ in range(2, n + 1):
            current_digits *= unique_digits
            count += current_digits
            unique_digits -= 1

        return count


# @lc code=end
def run():
    s = Solution()
    print("[SOLUTION]:", s.countNumbersWithUniqueDigits(3))


run()

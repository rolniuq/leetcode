#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (64.78%)
# Likes:    20438
# Dislikes: 1107
# Total Accepted:    2.8M
# Total Submissions: 4.3M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#
from typing import List


# @lc code=start
class Solution:
    def __init__(self):
        self.keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        pass

    def combine(self, index: int, path: str, res: List[str], digits):
        if index == len(digits):
            res.append(path)
            return

        letters = self.keys.get(digits[index])

        for letter in letters:
            path += letter

            self.combine(index + 1, path, res, digits)

            path = path[: len(path) - 1]

    def letterCombinations(self, digits: str) -> List[str]:
        path = ""
        res = []

        self.combine(0, path, res, digits)

        return res


# @lc code=end


def run():
    s = Solution()
    print("[SOLUTION]:", s.letterCombinations("23"))


run()

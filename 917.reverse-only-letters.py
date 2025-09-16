#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#


# @lc code=start
class Solution:
    def is_alphabet_ascii(self, char: str) -> bool:
        ascii_code = ord(char)
        if 65 <= ascii_code and ascii_code <= 90:
            return True
        elif 97 <= ascii_code and ascii_code <= 122:
            return True

        return False

    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        left, right = 0, len(s) - 1
        while left <= right:
            if not self.is_alphabet_ascii(s[left]):
                left += 1
            elif not self.is_alphabet_ascii(s[right]):
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)


# @lc code=end

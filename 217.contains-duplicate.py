#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict_ = {}
        for n in nums:
            if n in dict_:
                return True

            dict_[n] = 1

        return False

# @lc code=end


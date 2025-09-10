#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        pos = -1
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) is True:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1

        return pos


# @lc code=end

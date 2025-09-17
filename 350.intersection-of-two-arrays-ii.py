#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#


# @lc code=start
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res


# @lc code=end

#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        arr = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                arr.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums1[i])
                arr.append(nums2[j])
                i += 1
                j += 1

        while i < len(nums1):
            arr.append(nums1[i])
            i += 1

        while j < len(nums2):
            arr.append(nums2[j])
            j += 1

        res = arr[len(arr) // 2]

        if len(arr) % 2 == 0:
            mid = len(arr) // 2
            res = (arr[mid] + arr[mid - 1]) / 2

        return res


# @lc code=end

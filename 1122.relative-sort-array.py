#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#


# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        arr1.sort()
        arr1_dict = {}
        for i in range(len(arr1)):
            if arr1[i] not in arr1_dict:
                arr1_dict[arr1[i]] = 1
            else:
                arr1_dict[arr1[i]] += 1

        for i in range(len(arr2)):
            time = arr1_dict[arr2[i]]
            while time > 0:
                res.append(arr2[i])
                time -= 1

            arr1_dict[arr2[i]] = 0

        for key in arr1_dict:
            time = arr1_dict[key]
            while time > 0:
                res.append(key)
                time -= 1

        return res


# @lc code=end

from typing import List


class Solution:
    def array_to_map(self, nums: List[List[int]]) -> dict:
        res = {}
        for num in nums:
            res[num[0]] = num[1]

        return res

    def map_to_array(self, d: dict) -> List[List[int]]:
        res = []
        for key in d:
            res.append([key, d[key]])

        return res

    def sort_array(self, nums: List[List[int]]) -> List[List[int]]:
        return sorted(nums, key=lambda x: x[0])

    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        map_num_1 = self.array_to_map(nums1)
        map_num_2 = self.array_to_map(nums2)

        for key in map_num_2:
            if key in map_num_1:
                map_num_1[key] += map_num_2[key]
            else:
                map_num_1[key] = map_num_2[key]

        return self.sort_array(self.map_to_array(map_num_1))

    def two_pointer(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        i = 0
        j = 0
        result = []

        while (i < len(nums1)) and (j < len(nums2)):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            if id1 < id2:
                result.append([id1, val1])
                i += 1
            elif id1 > id2:
                result.append([id2, val2])
                j += 1
            else:
                result.append([id1, val1 + val2])
                i += 1
                j += 1

        while i < len(nums1):
            id1, val1 = nums1[i]
            result.append([id1, val1])
            i += 1

        while j < len(nums2):
            id2, val2 = nums2[j]
            result.append([id2, val2])
            j += 1

        return result

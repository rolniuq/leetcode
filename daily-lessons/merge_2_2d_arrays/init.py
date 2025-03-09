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

    def merge_array(
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

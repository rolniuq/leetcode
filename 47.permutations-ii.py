#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.42%)
# Likes:    8995
# Dislikes: 159
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#
from typing import List


# @lc code=start
class Solution:
    def permute(self, index: int, nums: List[int], res: List[List[int]]):
        if index == len(nums):
            res.append(nums.copy())
            return

        used = set()

        for i in range(index, len(nums)):
            if nums[i] in used:
                continue

            used.add(nums[i])

            nums[index], nums[i] = nums[i], nums[index]
            self.permute(index + 1, nums, res)
            nums[index], nums[i] = nums[i], nums[index]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.permute(0, nums, res)
        return res


# @lc code=end
def run():
    s = Solution()
    # l = list([1, 2, 3])
    # l = list([1, 1, 2])
    l = list([3, 3, 0, 3])  # [[0,3,3,3],[3,0,3,3],[3,3,0,3],[3,3,3,0]]
    print("[SOLUTION]:", s.permuteUnique(l))


run()

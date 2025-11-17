#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (58.40%)
# Likes:    11980
# Dislikes: 373
# Total Accepted:    1.6M
# Total Submissions: 2.7M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# Constraints:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
#
#
from typing import List


# @lc code=start
class Solution:
    def combine(
        self,
        index: int,
        path: List[int],
        res: List[List[int]],
        candidates: List[int],
        target: int,
        total: int,
    ):
        if total == target:
            res.append(path.copy())
            return

        if index == len(candidates) or total > target:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            path.append(candidates[i])
            self.combine(i + 1, path, res, candidates, target, total + candidates[i])
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path, res = [], []
        candidates.sort()
        self.combine(0, path, res, candidates, target, 0)
        return res


# @lc code=end
def run():
    s = Solution()
    l = list([2, 5, 2, 1, 2])
    target = 5
    print(
        "[SOLUTION]:",
        s.combinationSum2(l, target),
    )


run()

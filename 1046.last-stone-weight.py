#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#


# @lc code=start
import math


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        counter = 0
        while len(stones) > 1:
            first_max, second_max = -math.inf, -math.inf
            first_max_idx, second_max_idx = -1, -1

            while counter < len(stones):
                print(counter, stones, first_max, second_max)
                if stones[counter] > first_max:
                    second_max = first_max
                    first_max = stones[counter]
                    second_max_idx = first_max_idx
                    first_max_idx = counter
                elif second_max <= stones[counter] <= first_max:
                    second_max = stones[counter]
                    second_max_idx = counter

                counter += 1

            stones[first_max_idx] = stones[first_max_idx] - stones[second_max_idx]
            stones.pop(second_max_idx)
            counter = 0

        return 0 if len(stones) == 0 else stones[0]


# @lc code=end

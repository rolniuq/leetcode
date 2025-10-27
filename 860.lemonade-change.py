#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#


# @lc code=start
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollars = 0
        ten_dollars = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five_dollars += 1
            elif bills[i] == 10:
                if five_dollars == 0:
                    return False

                ten_dollars += 1
                five_dollars -= 1
            elif bills[i] == 20:
                if ten_dollars > 0 and five_dollars > 0:
                    ten_dollars -= 1
                    five_dollars -= 1
                elif ten_dollars == 0 and five_dollars > 0:
                    if five_dollars < 3:
                        return False
                    else:
                        five_dollars -= 3
                else:
                    return False

        return True


# @lc code=end
def run():
    s = Solution()
    # bills = list([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5])
    bills = list([5, 5, 10, 10, 20])
    print("[SOLUTION]", s.lemonadeChange(bills))


run()

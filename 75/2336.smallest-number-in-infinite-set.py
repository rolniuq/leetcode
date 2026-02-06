#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#
# https://leetcode.com/problems/smallest-number-in-infinite-set/description/
#
# algorithms
# Medium (70.57%)
# Likes:    1839
# Dislikes: 232
# Total Accepted:    224.6K
# Total Submissions: 318.3K
# Testcase Example:  '["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"]\n' +
#  '[[],[2],[],[],[],[1],[],[],[]]'
#
# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
#
# Implement the SmallestInfiniteSet class:
#
#
# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain
# all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the
# infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set,
# if it is not already in the infinite set.
#
#
#
# Example 1:
#
#
# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest",
# "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]
#
# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change
# is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest
# number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the
# set and
# ⁠                                  // is the smallest number, and remove it
# from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the
# set.
#
#
#
# Constraints:
#
#
# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.
#
#
#

# @lc code=start
class Heap:
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index] >= self.data[parent]:
                break

            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    def peek(self):
        if not self.data:
            return None

        return self.data[0]

    def pop(self):
        if not self.data:
            return None

        res = self.data[0]
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.data = self.data[: len(self.data) - 1]

        self.heapify_down(0)

        return res

    def heapify_down(self, index):
        if not self.data:
            return

        size = len(self.data)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.data[smallest] > self.data[left]:
                smallest = left
            if right < size and self.data[smallest] > self.data[right]:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index],
            )
            index = smallest


class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.heap = Heap()
        self.added = {}

    def popSmallest(self) -> int:
        res = self.heap.peek()
        if res:
            self.heap.pop()
            del self.added[res]
            return res

        res = self.current
        self.current += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added:
            self.heap.insert(num)
            self.added[num] = True


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

/*
* @lc app=leetcode id=2336 lang=golang
*
* [2336] Smallest Number in Infinite Set
*
* https://leetcode.com/problems/smallest-number-in-infinite-set/description/
*
  - algorithms
  - Medium (70.57%)
  - Likes:    1839
  - Dislikes: 232
  - Total Accepted:    224.6K
  - Total Submissions: 318.3K
  - Testcase Example:  '["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"]\n' +
    '[[],[2],[],[],[],[1],[],[],[]]'

*
* You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
*
* Implement the SmallestInfiniteSet class:
*
*
* SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain
* all positive integers.
* int popSmallest() Removes and returns the smallest integer contained in the
* infinite set.
* void addBack(int num) Adds a positive integer num back into the infinite
* set, if it is not already in the infinite set.
*
*
*
* Example 1:
*
*
* Input
* ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest",
* "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
* [[], [2], [], [], [], [1], [], [], []]
* Output
* [null, null, 1, 2, 3, null, 1, 4, 5]
*
* Explanation
* SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
* smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change
* is made.
* smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest
* number, and remove it from the set.
* smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
* smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
* smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
* smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to
* the set and
* ⁠                                  // is the smallest number, and remove it
* from the set.
* smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
* smallestInfiniteSet.popSmallest(); // return 5, and remove it from the
* set.
*
*
*
* Constraints:
*
*
* 1 <= num <= 1000
* At most 1000 calls will be made in total to popSmallest and addBack.
*
*
*/
package lc

// @lc code=start
type MinHeap2336 struct {
	data []int
}

func (h *MinHeap2336) Insert(val int) {
	h.data = append(h.data, val)
	h.heapifyUp(len(h.data) - 1)
}

func (h *MinHeap2336) heapifyUp(index int) {
	// root
	if index == 0 {
		return
	}

	for {
		parent := (index - 1) / 2
		if h.data[index] >= h.data[parent] {
			break
		}

		h.data[index], h.data[parent] = h.data[parent], h.data[index]
		index = parent
	}
}

func (h *MinHeap2336) Peek() (int, bool) {
	if len(h.data) == 0 {
		return 0, false
	}

	return h.data[0], true
}

func (h *MinHeap2336) Pop() (int, bool) {
	if len(h.data) == 0 {
		return 0, false
	}

	res := h.data[0]
	last := h.data[len(h.data)-1]
	h.data[0], h.data[len(h.data)-1] = last, res
	h.data = h.data[:len(h.data)-1]

	h.heapifyDown(0)

	return res, true
}

func (h *MinHeap2336) heapifyDown(index int) {
	size := len(h.data)

	for {
		smallest := index
		left, right := 2*index+1, 2*index+2

		if left < size && h.data[left] < h.data[smallest] {
			smallest = left
		}
		if right < size && h.data[right] < h.data[smallest] {
			smallest = right
		}
		if smallest == index {
			break
		}

		h.data[index], h.data[smallest] = h.data[smallest], h.data[index]
		index = smallest
	}
}

type SmallestInfiniteSet struct {
	current int
	heap    MinHeap2336
	added   map[int]bool
}

func Constructor() SmallestInfiniteSet {
	return SmallestInfiniteSet{
		current: 1,
		heap:    MinHeap2336{data: []int{}},
		added:   make(map[int]bool),
	}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	res, ok := this.heap.Peek()
	if ok && res < this.current {
		this.heap.Pop()
		delete(this.added, res)
		return res
	}

	res = this.current
	this.current++
	return res
}

func (this *SmallestInfiniteSet) AddBack(num int) {
	if num < this.current && !this.added[num] {
		this.heap.Insert(num)
		this.added[num] = true
	}
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.PopSmallest();
 * obj.AddBack(num);
 */
// @lc code=end

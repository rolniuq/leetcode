/*
 * @lc app=leetcode id=215 lang=golang
 *
 * [215] Kth Largest Element in an Array
 *
 * https://leetcode.com/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (68.67%)
 * Likes:    18560
 * Dislikes: 968
 * Total Accepted:    3.4M
 * Total Submissions: 5M
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * Given an integer array nums and an integer k, return the k^th largest
 * element in the array.
 *
 * Note that it is the k^th largest element in the sorted order, not the k^th
 * distinct element.
 *
 * Can you solve it without sorting?
 *
 *
 * Example 1:
 * Input: nums = [3,2,1,5,6,4], k = 2
 * Output: 5
 * Example 2:
 * Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
 * Output: 4
 *
 *
 * Constraints:
 *
 *
 * 1 <= k <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 *
 *
 */
package lc

// @lc code=start
type MinHeap struct {
	data []int
}

func (h *MinHeap) Insert(val int) {
	h.data = append(h.data, val)
	h.heapifyUp(len(h.data) - 1)
}

func (h *MinHeap) heapifyUp(index int) {
	for index > 0 {
		parent := (index - 1) / 2

		if h.data[index] >= h.data[parent] {
			break
		}

		h.data[index], h.data[parent] = h.data[parent], h.data[index]
		index = parent
	}
}

func (h *MinHeap) Peek() (int, bool) {
	if h == nil || len(h.data) == 0 {
		return 0, false
	}

	return h.data[0], true
}

func (h *MinHeap) heapifyDown(index int) {
	size := len(h.data)
	smallest := index

	for {
		left := 2*index + 1
		right := 2*index + 2

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

func (h *MinHeap) Pop() (int, bool) {
	if h == nil || len(h.data) == 0 {
		return 0, false
	}

	root := h.data[0]

	h.data[0], h.data[len(h.data)-1] = h.data[len(h.data)-1], h.data[0]
	h.data = h.data[:len(h.data)-1]

	h.heapifyDown(0)

	return root, true
}

func findKthLargest(nums []int, k int) int {
	minHeap := &MinHeap{data: make([]int, 0, k)}

	for _, num := range nums {
		minHeap.Insert(num)

		if len(minHeap.data) > k {
			minHeap.Pop()
		}
	}

	if val, ok := minHeap.Peek(); ok {
		return val
	}

	return 0
}

// @lc code=end

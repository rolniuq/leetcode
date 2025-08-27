/*
 * @lc app=leetcode id=66 lang=golang
 *
 * [66] Plus One
 */
package leetcode

// @lc code=start
func addEleToArr(arr []int, ele, index int) []int {
	if len(arr) == 0 {
		return arr
	}

	for i := 0; i < len(arr); i++ {
		if i == index {
			arr = append(arr, 0)
			for j := index; j < len(arr)-1; j++ {
				arr[j+1] = arr[j]
			}
			arr[index] = ele

			break
		}
	}

	return arr
}

func plusOne(digits []int) []int {
	last := digits[len(digits)-1]
	if last < 9 {
		digits[len(digits)-1] = last + 1
		return digits
	}

	counter := 0
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] == 9 {
			digits[i] = 0
			counter++
		} else {
			digits[i] = digits[i] + 1
			counter = 0
			break
		}
	}

	if counter == 0 {
		return digits
	}

	return addEleToArr(digits, 1, len(digits)-counter)
}

// @lc code=end

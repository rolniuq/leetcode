/*
 * @lc app=leetcode id=67 lang=golang
 *
 * [67] Add Binary
 *
 * https://leetcode.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (56.36%)
 * Likes:    10235
 * Dislikes: 1080
 * Total Accepted:    2M
 * Total Submissions: 3.6M
 * Testcase Example:  '"11"\n"1"'
 *
 * Given two binary strings a and b, return their sum as a binary string.
 *
 *
 * Example 1:
 * Input: a = "11", b = "1"
 * Output: "100"
 * Example 2:
 * Input: a = "1010", b = "1011"
 * Output: "10101"
 *
 *
 * Constraints:
 *
 *
 * 1 <= a.length, b.length <= 10^4
 * a and b consist only of '0' or '1' characters.
 * Each string does not contain leading zeros except for the zero itself.
 *
 *
 */

package leetcode

import (
	"fmt"
	"strconv"
)

// @lc code=start
func addZero(str string, l int) string {
	for range l {
		str = "0" + str
	}

	return str
}

func addBinary(a string, b string) string {
	if len(b) > len(a) {
		a, b = b, a
	}

	b = addZero(b, len(a)-len(b))

	res := ""
	exist := 0

	for i := len(a) - 1; i >= 0; i-- {
		num_a, _ := strconv.ParseInt(string(a[i]), 10, 64)
		num_b, _ := strconv.ParseInt(string(b[i]), 10, 64)

		sum := int(num_a) + int(num_b) + exist
		if sum == 2 {
			res = "0" + res
			exist = 1
		} else {
			res = fmt.Sprintf("%d%s", sum%2, res)
			exist = sum / 2
		}
	}

	if exist > 0 {
		res = fmt.Sprintf("%d%s", exist, res)
	}

	return res
}

// @lc code=end

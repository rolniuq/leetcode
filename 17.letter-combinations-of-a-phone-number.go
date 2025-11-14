/*
 * @lc app=leetcode id=17 lang=golang
 *
 * [17] Letter Combinations of a Phone Number
 *
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (64.78%)
 * Likes:    20438
 * Dislikes: 1107
 * Total Accepted:    2.8M
 * Total Submissions: 4.3M
 * Testcase Example:  '"23"'
 *
 * Given a string containing digits from 2-9 inclusive, return all possible
 * letter combinations that the number could represent. Return the answer in
 * any order.
 *
 * A mapping of digits to letters (just like on the telephone buttons) is given
 * below. Note that 1 does not map to any letters.
 *
 *
 * Example 1:
 *
 *
 * Input: digits = "23"
 * Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
 *
 *
 * Example 2:
 *
 *
 * Input: digits = "2"
 * Output: ["a","b","c"]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= digits.length <= 4
 * digits[i] is a digit in the range ['2', '9'].
 *
 *
 */
package leetcode

// @lc code=start

var mapPhone = map[byte]string{
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
}

func backTracking(index int, res *[]string, path *[]byte, digits string) {
	if index == len(digits) {
		*res = append(*res, string(*path))
		return
	}

	letters := mapPhone[digits[index]]

	for i := range len(letters) {
		*path = append(*path, letters[i])

		backTracking(index+1, res, path, digits)

		pVal := *path
		*path = pVal[:len(pVal)-1]
	}
}

func letterCombinations(digits string) []string {
	res := []string{}
	path := []byte{}

	backTracking(0, &res, &path, digits)

	return res
}

// @lc code=end

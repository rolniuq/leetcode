/*
 * @lc app=leetcode id=345 lang=golang
 *
 * [345] Reverse Vowels of a String
 *
 * https://leetcode.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (60.05%)
 * Likes:    5242
 * Dislikes: 2850
 * Total Accepted:    1.5M
 * Total Submissions: 2.5M
 * Testcase Example:  '"IceCreAm"'
 *
 * Given a string s, reverse only all the vowels in the string and return it.
 *
 * The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
 * lower and upper cases, more than once.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "IceCreAm"
 *
 * Output: "AceCreIm"
 *
 * Explanation:
 *
 * The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes
 * "AceCreIm".
 *
 *
 * Example 2:
 *
 *
 * Input: s = "leetcode"
 *
 * Output: "leotcede"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s consist of printable ASCII characters.
 *
 *
 */
package lc

import "strings"

// @lc code=start
func reverseVowels(s string) string {
	vowels := "aeiouAEIOU"
	runes := []rune(s)
	left := 0
	right := len(s) - 1
	for left < right {
		leftFlag := strings.Contains(vowels, string(s[left]))
		rightFlag := strings.Contains(vowels, string(s[right]))
		if !leftFlag {
			left++
			continue
		}
		if !rightFlag {
			right--
			continue
		}

		runes[left], runes[right] = runes[right], runes[left]
		left++
		right--
	}

	return string(runes)
}

// @lc code=end

/*
 * @lc app=leetcode id=1456 lang=golang
 *
 * [1456] Maximum Number of Vowels in a Substring of Given Length
 *
 * https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
 *
 * algorithms
 * Medium (61.30%)
 * Likes:    3868
 * Dislikes: 151
 * Total Accepted:    637.9K
 * Total Submissions: 1M
 * Testcase Example:  '"abciiidef"\n3'
 *
 * Given a string s and an integer k, return the maximum number of vowel
 * letters in any substring of s with length k.
 *
 * Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abciiidef", k = 3
 * Output: 3
 * Explanation: The substring "iii" contains 3 vowel letters.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "aeiou", k = 2
 * Output: 2
 * Explanation: Any substring of length 2 contains 2 vowels.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "leetcode", k = 3
 * Output: 2
 * Explanation: "lee", "eet" and "ode" contain 2 vowels.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists of lowercase English letters.
 * 1 <= k <= s.length
 *
 *
 */
package lc

import "strings"

// @lc code=start
func isVowels(r string) bool {
	return strings.Contains("aeiou", r)
}

func getVowels(t string) int {
	count := 0

	for _, v := range t {
		if isVowels(string(v)) {
			count++
		}
	}

	return count
}

func maxVowels(s string, k int) int {
	sub := s[:k]
	cur_sub := getVowels(sub)
	max := cur_sub

	for i := 1; i <= len(s)-k; i++ {
		prev := s[i-1]
		if isVowels(string(prev)) {
			cur_sub -= 1
		}
		next := s[i+k-1]
		if isVowels(string(next)) {
			cur_sub += 1
		}

		if cur_sub > max {
			max = cur_sub
		}
	}

	return max
}

// @lc code=end

/*
 * @lc app=leetcode id=1071 lang=golang
 *
 * [1071] Greatest Common Divisor of Strings
 *
 * https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
 *
 * algorithms
 * Easy (53.08%)
 * Likes:    5936
 * Dislikes: 1647
 * Total Accepted:    898.2K
 * Total Submissions: 1.7M
 * Testcase Example:  '"ABCABC"\n"ABC"'
 *
 * For two strings s and t, we say "t divides s" if and only if s = t + t + t +
 * ... + t + t (i.e., t is concatenated with itself one or more times).
 *
 * Given two strings str1 and str2, return the largest string x such that x
 * divides both str1 and str2.
 *
 *
 * Example 1:
 *
 *
 * Input: str1 = "ABCABC", str2 = "ABC"
 *
 * Output: "ABC"
 *
 *
 * Example 2:
 *
 *
 * Input: str1 = "ABABAB", str2 = "ABAB"
 *
 * Output: "AB"
 *
 *
 * Example 3:
 *
 *
 * Input: str1 = "LEET", str2 = "CODE"
 *
 * Output: ""
 *
 *
 * Example 4:
 *
 *
 * Input: str1 = "AAAAAB", str2 = "AAA"
 *
 * Output: ""​​​​​​​
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= str1.length, str2.length <= 1000
 * str1 and str2 consist of English uppercase letters.
 *
 *
 */
package lc

// @lc code=start
func gcd(a, b int) int {
	if b == 0 {
		return a
	}

	return gcd(b, a%b)
}

func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}

	v := gcd(len(str1), len(str2))

	// str1[:v] or str2[:v] is the same result

	return str2[:v]
}

// @lc code=end

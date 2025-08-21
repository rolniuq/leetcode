/*
 * @lc app=leetcode id=9 lang=rust
 *
 * [9] Palindrome Number
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false
        }

        let mut y = x;
        let mut res = 0;

        while y > 0 {
            res = res * 10 + y%10;
            y /= 10;
        }

        return res == x
    }
}

// @lc code=end


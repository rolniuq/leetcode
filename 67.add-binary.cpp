/*
 * @lc app=leetcode id=67 lang=cpp
 *
 * [67] Add Binary
 */

// @lc code=start
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    void addZero(string *a, int plus) {
        a->insert(0, plus, '0');
    }

    string addBinary(string a, string b) {
        int gap = 0;
        if (a.length() > b.length()) {
            gap = a.length() - b.length();
            addZero(&b, gap);
        } else {
            gap = b.length() - a.length();
            addZero(&a, gap);
        }

        string result;
        int exist = 0;
        for (int i = a.length() - 1; i >= 0; i--) {
            int bitA = a[i] - '0';
            int bitB = b[i] - '0';

            int sum = bitA + bitB + exist;
            if (sum == 2) {
                result += '0';
                exist = 1;
            } else {
                cout << "x" <<  sum%2 << endl;
                result += (sum%2) + '0';
                exist = sum/2;
            }
        }

        if (exist) {
            result += '1';
        }

        reverse(result.begin(), result.end());

        return result;
    }
};
// @lc code=end

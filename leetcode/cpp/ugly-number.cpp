// https://leetcode.com/problems/ugly-number/

class Solution {
public:
    bool isUgly(int num) {
        if (num < 1) {
            return false;
        }

        int set[] = {2, 3, 5},
            i = 0;

        for (i = 0; i < 3; ++i) {
            while (num % set[i] == 0) {
                num /= set[i];
            }
        }

        return (num == 1);
    }
};

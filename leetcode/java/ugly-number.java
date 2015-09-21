// https://leetcode.com/problems/ugly-number/

public class Solution {
    public boolean isUgly(int num) {
        if (num < 1) {
            return false;
        }

        int[] set = new int[] {2, 3, 5};
        for (int factor: set) {
            while (num % factor == 0) {
                num /= factor;
            }
        }

        return (num == 1);
    }
}

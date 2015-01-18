#!/usr/bin/python


# https://oj.leetcode.com/problems/reverse-integer/
class Solution:
    # @return an integer
    def reverse(self, x):
        f = x > 0
        if not f:
            x *= -1

        r = int(''.join(reversed(list(str(x)))))

        if r > 2147483647:
            return 0

        if not f:
            r *= -1

        return r

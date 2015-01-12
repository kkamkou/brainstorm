#!/usr/bin/python


# https://oj.leetcode.com/problems/excel-sheet-column-number/
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        r = 0
        for c in s:
            r = r * 26 + (ord(c) - 64)
        return r

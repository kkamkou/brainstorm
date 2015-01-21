#!/usr/bin/python


# https://oj.leetcode.com/problems/single-number/
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        r = 0
        for i in A:
            r ^= i
        return r

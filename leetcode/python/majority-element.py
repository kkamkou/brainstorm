#!/usr/bin/python


# https://oj.leetcode.com/problems/majority-element/
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        # return sorted(num)[len(num) / 2]

        # return max(set(num), key=num.count)

        m = len(num) / 2
        d = {}

        for n in num:
            s = str(n)

            d[s] = d.get(s, 0) + 1
            if d[s] > m:
                return n

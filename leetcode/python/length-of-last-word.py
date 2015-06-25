#!/usr/bin/python


# https://leetcode.com/problems/length-of-last-word/
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        return len(s.rstrip().split(' ')[-1])
        # return len(s[::-1].lstrip().split(' ')[0])

#!/usr/bin/python


# https://oj.leetcode.com/problems/implement-strstr/
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        return haystack.find(needle)
        """
            try:
                return haystack.index(needle)
            except:
                return -1
        """

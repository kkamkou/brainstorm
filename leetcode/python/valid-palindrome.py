#!/usr/bin/python


# https://oj.leetcode.com/problems/valid-palindrome/
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        # The fastest variant:
        # s = filter(str.isalnum, s.lower())
        # return s == s[::-1]

        if not s:
            return True

        s = s.lower()

        cl = 0
        cr = len(s)-1
        while cl <= cr:
            if not s[cl].isalnum():
                cl += 1
                continue

            if not s[cr].isalnum():
                cr -= 1
                continue

            if s[cl] != s[cr]:
                return False

            cl += 1
            cr -= 1

        return True

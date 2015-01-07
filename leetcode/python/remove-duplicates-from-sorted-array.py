#!/usr/bin/python


# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        k = 1;
        for v in range(1, len(A)):
            if A[v-1] != A[v]:
                A[k] = A[v]
                k += 1

        return k

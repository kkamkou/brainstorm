#!/usr/bin/python


# https://oj.leetcode.com/problems/rotate-array/
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        l = len(nums)

        k %= l
        if k == 0:
            return

        g = l - k;
        self.__reverse(nums, 0, g);
        self.__reverse(nums, g, l);
        self.__reverse(nums, 0, l);

    def __reverse(self, nums, s, e):
        e -= 1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

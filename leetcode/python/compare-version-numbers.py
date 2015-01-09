#!/usr/bin/python


# https://oj.leetcode.com/problems/compare-version-numbers/
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        version1 = self.__normalize(version1)
        version2 = self.__normalize(version2)

        v1l = len(version1)
        v2l = len(version2)
        if v1l > v2l:
            version2 += [0] * (v1l - v2l)
        elif v2l > v1l:
            version1 += [0] * (v2l - v1l)

        for n in range(len(version2)):
            if version1[n] == version2[n]:
                continue
            if version1[n] > version2[n]:
                return 1
            elif version2[n] > version1[n]:
                return -1

        return 0

    def __normalize(self, v):
        if v.find('.') == -1:
            return [int(v)]
        return map(int, v.split('.'))


#!/usr/bin/python


# https://oj.leetcode.com/problems/majority-element/
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        # return sorted(num)[len(num) / 2]

        # return max(set(num), key=num.count)

        """
        m = len(num) / 2
        d = {}

        for n in num:
            s = str(n)

            d[s] = d.get(s, 0) + 1
            if d[s] > m:
                return n
        """

        r = 0

        for d in range(32):
            o = 0; z = 0

            for e in num:
                if ((e & (1 << d)) != 0):
                    o += 1
                else:
                    z += 1

            if o > z:
                r |= (1 << d)

            """
                Py' int has no overflow, it is converted to long automatically.
                Py3 has no long at all. Only int: http://python3porting.com/differences.html
            """
            if r & 0x80000000:
                r = -((r^0xffffffff) + 1)
                #r = -0x100000000 + r

        return r

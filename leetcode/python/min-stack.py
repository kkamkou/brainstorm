#!/usr/bin/python


# https://oj.leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.sc = []
        self.sm = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.sc.append(x)
        if x <= self.getMin():
            self.sm.append(x)
        return x

    # @return nothing
    def pop(self):
        if self.sc.pop() == self.getMin():
            self.sm.pop()

    # @return an integer
    def top(self):
        return self.sc[-1]

    # @return an integer
    def getMin(self):
        try:
            return self.sm[-1]
        except IndexError:
            return self.top()

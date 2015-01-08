#!/usr/bin/python


# https://oj.leetcode.com/problems/min-stack/
class MinStack:
    min = None

    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if self.min == None:
            self.min = x
        elif self.min > x:
            self.min = x
        return x

    # @return nothing
    def pop(self):
        v = self.stack.pop()
        if v == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = None

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min

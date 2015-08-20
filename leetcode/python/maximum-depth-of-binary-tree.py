#!/usr/bin/python


# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

"""
class Solution(object):
    def maxDepth(self, root):
        res = 0
        lst = [(root, 0)]
        while lst:
            leaf, lvl = lst.pop()
            if leaf:
                lst.append((leaf.left, lvl + 1))
                lst.append((leaf.right, lvl + 1))
                continue
            res = max(res, lvl)
        return res
"""

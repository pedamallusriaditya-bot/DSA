class Solution(object):
    def numTrees(self, n):
        c = 1
        for i in range(n):
            c = c * 2 * (2 * i + 1) // (i + 2)
        return c
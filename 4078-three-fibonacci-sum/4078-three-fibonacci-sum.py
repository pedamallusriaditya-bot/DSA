class Solution(object):
    def threeFibonacciSum(self, n):
        if n % 2 != 0:
            return False
        target = n // 2
        a, b = 0, 1
        while b < target:
            a, b = b, a + b
        return b == target
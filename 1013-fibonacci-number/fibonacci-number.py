class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1, n2, n3 = 0, 1, 0
        while n > 0:
            n3 = n1
            n1 = n1 + n2
            n2 = n3
            n -= 1
        return n1
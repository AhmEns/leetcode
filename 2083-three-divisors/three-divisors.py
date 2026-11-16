class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i, return_val = 1, 0
        while i <= n:
            if n % i == 0:
                return_val += 1
            i += 1
        return return_val == 3
        
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, sum = 1, 0
        digits = []

        while n > 0:
            digits.append(n % 10)
            n = n / 10

        for i in digits:
            product *= i
            sum += i
        
        return product - sum
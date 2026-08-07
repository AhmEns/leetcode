class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        
        rev = int(str(abs(x))[::-1])
        
        if neg:
            rev = -rev
            
        if rev > 2147483647 or rev < -2147483648:
            return 0
            
        return rev
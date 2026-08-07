class Solution(object):
    def reverse(self, x):
        neg = x < 0
        x = abs(x)
        rev = 0
        
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
            
        if neg:
            rev = -rev
            
        if rev > 2147483647 or rev < -2147483648:
            return 0
            
        return rev
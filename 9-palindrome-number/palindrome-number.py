class Solution(object):
    def isPalindrome(self, x):
        if -2**31 > x or 2**31 - 1 < x:
            return False
        else:
            x = str(x)
            reversed = x[::-1]
            if reversed == x:
                return True
            else:
                return False

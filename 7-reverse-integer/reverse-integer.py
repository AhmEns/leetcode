class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        s = list(str(abs(x)))
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
                
        rev = int("".join(s))
        if neg:
            rev = -rev

        if rev > 2147483647 or rev < -2147483648:
            return 0
        return rev
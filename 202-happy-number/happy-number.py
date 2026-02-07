class Solution(object):
    def isHappy(self, n):
        used = set()

        if n == 1:
            return True
        else:
            while n != 1:
                n = sum(int(digit)**2 for digit in str(n))

                if n in used:
                    return False
                elif n == 1:
                    return True
                else:
                    used.add(n)            

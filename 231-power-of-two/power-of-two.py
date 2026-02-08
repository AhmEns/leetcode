class Solution(object):
    def isPowerOfTwo(self, n):
        power = -31
        isTrue = False
        while power < 32:
            if 2**power == n:
                isTrue = True
            power += 1
        return isTrue
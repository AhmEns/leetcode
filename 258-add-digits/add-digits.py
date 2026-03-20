class Solution(object):
    def addDigits(self, num):
        n = 0
        while True:
            while 0 < num:
                n = (num % 10) + n
                num = num // 10
            if n < 10:
                return n
            num = n
            n = 0
            
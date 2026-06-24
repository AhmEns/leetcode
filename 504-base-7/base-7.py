class Solution(object):
    def convertToBase7(self, num):
        if num == 0:    
            return "0"
        elif num < 0:
            num = abs(num)
            res = ""
            while num > 0:
                res = str(num % 7) + res
                num //= 7
            return "-" + res
        else:
            res = ""
            while num > 0:
                res = str(num % 7) + res
                num //= 7
            return res
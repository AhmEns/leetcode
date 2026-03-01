class Solution(object):
    def singleNumber(self, nums):
        temp = 0
        for i in nums:
            temp ^= i
        return temp
            
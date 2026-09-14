class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return_val = []
        for i in nums:
            if i % 2 == 0:
                return_val.append(i)
        for i in nums:
            if i % 2 != 0:
                return_val.append(i)
        return return_val

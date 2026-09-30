class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return_val = []
        n = 0
        for i in nums:
            for j in nums:
                if j < i:
                    n += 1
            return_val.append(n)
            n = 0
        return return_val

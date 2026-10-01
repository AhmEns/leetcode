class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)

        return_val = nums[0]

        for i in nums[1:]:
            return_val ^= i
        
        return return_val
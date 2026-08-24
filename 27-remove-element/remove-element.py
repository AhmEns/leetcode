class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        return_val = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[return_val] = nums[i]
                return_val += 1    
            
        return return_val
            
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        artan = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                break
            elif nums[i] > nums[i + 1]:
                artan = False
                break

        if artan == True:    
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        else:
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
            return True
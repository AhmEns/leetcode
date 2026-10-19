class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return_val = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                return_val.append(i)
        
        return return_val
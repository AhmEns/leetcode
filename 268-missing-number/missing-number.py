class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        nums_set = set(range(0, len(nums) + 1))

        for i in nums:
            if i in nums_set:
                nums_set.remove(i)

        return_val = nums_set.pop()
        return return_val
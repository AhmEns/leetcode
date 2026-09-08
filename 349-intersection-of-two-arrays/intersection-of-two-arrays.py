class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return_val = []
        
        kume = set(nums2)

        for num in nums1:
            if num in kume and num not in return_val:
                return_val.append(num)
        return return_val
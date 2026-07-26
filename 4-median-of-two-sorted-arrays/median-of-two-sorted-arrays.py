class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged = sorted(merged)
        if len(merged) % 2 == 1:
            return merged[(len(merged) - 1) / 2]
        else:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2.0
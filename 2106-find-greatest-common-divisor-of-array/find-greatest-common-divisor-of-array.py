class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest, largest = 1000, 0
        for i in nums:
            if i < smallest:
                smallest = i
            if i > largest:
                largest = i
        while smallest != 0:
            largest, smallest = smallest, largest % smallest
        return largest
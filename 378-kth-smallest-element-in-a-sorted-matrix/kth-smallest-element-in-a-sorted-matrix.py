class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        combined = []
        for i in matrix:
            combined.extend(i)
        combined.sort()
        return combined[k - 1]
class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Sum each row in the adjacency matrix to get the degree of each vertex
        return [sum(row) for row in matrix]
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        left, right, sum = 0, len(mat) - 1, 0
        for i in mat:
            if left != right:
                sum += i[left]
                sum += i[right]
            else:
                sum += i[left]
            left += 1
            right -= 1
        return sum
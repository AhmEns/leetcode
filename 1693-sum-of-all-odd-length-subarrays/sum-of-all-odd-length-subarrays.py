class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum, n = 0, 1

        while n <= len(arr):
            for i in range(len(arr)):
                if i + n - 1 < len(arr):
                    k = n - 1
                    while k >= 0:
                        sum += arr[i + k]
                        k -= 1
            n += 2
        return sum
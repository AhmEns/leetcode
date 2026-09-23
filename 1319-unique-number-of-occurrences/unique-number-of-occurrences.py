class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = []
        count = 0
        arr.sort()
        
        for i in range(len(arr)):
            if i < len(arr) - 1 and arr[i] == arr[i + 1]:
                count += 1
            else:
                counts.append(count + 1)
                count = 0
                
        counts.sort()
        
        for i in range(len(counts) - 1):
            if counts[i] == counts[i + 1]:
                return False
                
        return True
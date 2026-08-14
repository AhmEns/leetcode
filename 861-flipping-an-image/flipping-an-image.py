class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for i in image:
            left, right = 0, len(i)- 1
            while left < right:
                i[left], i[right] = i[right], i[left]
                left += 1
                right -= 1
        for i in image:
            n = 0
            while n < len(i):
                if i[n] == 1:
                    i[n] = 0
                else:
                    i[n] = 1
                n += 1
        return image
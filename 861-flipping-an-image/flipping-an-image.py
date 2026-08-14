class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for i in image:
            left, right = 0, len(i)- 1
            while left <= right:
                i[left], i[right] = i[right] ^ 1, i[left] ^ 1
                left += 1
                right -= 1
        return image
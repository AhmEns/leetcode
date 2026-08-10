class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, area = 0, len(height) - 1, 0
        
        while left < right:
            if height[right] >= height[left] and height[left] * (right - left) > area:
                    area = height[left] * (right - left)
            elif height[left] > height[right] and height[right] * (right - left) > area:
                    area = height[right] * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                 right -= 1
        return area
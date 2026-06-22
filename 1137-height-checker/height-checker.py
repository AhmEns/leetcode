class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        n = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                n = n + 1
        return n
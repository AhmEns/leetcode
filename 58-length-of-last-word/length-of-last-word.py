class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = [word for word in s.split(' ') if word]
        
        if not words:
            return 0
        
        return len(words[-1])
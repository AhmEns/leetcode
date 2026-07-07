class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
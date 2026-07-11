class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        reverse = []
        for i in range(len(s) - 1, -1, -1):
            reverse.append(s[i])
        for i in range(len(s)):
            s[i] = reverse[i]
        return reverse[i]
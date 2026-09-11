class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                start1, end, start2 = i, len(needle), 0
                while end >= 0 and start1 < len(haystack):
                    if haystack[start1] == needle[start2]:
                        start1 += 1
                        start2 += 1
                        end -= 1
                        if start2 == len(needle):
                            return i
                    else:
                        break
                        
        return -1
                
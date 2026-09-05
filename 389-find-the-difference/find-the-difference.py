class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_list = list(t)
        for i in s:
            t_list.remove(i)

        return t_list[0]
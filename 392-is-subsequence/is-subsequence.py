class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False

        s_index = 0
        t_index = 0

        while t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
                if s_index == len(s):
                    return True
            t_index += 1

        return False    
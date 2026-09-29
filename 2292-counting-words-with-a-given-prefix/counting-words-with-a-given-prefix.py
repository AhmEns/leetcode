class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return_val = 0
        for i in words:
            if i.startswith(pref):
                return_val += 1
        return return_val
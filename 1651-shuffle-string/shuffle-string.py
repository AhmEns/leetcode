class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        return_val = [None] * len(indices)
        for i in indices:
            return_val[indices[i]] = s[i]

        return "".join(return_val)
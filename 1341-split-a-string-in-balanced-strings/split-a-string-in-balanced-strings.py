class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        return_value, counter = 0, 0
        for i in s:
            if i == "R":
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                return_value += 1
        return return_value
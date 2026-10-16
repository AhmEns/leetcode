class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        return_val, wealth = 0, 0

        for i in accounts:
            for j in i:
                wealth += j
            if wealth > return_val:
                return_val = wealth
            wealth = 0
        
        return return_val
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        min = 0
        for i in range(len(prices)):
            if prices[i] < prices[min]:
                min = i
            elif prices[i] - prices[min] > max:
                max = prices[i] - prices[min]
        return max
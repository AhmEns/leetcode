class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        return_value = 0
        remainder = 0
        while numBottles > 0:
            return_value += numBottles
            numBottles += remainder
            remainder = numBottles % numExchange
            numBottles = numBottles // numExchange
        return return_value

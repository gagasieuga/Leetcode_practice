class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            potentialProfit = price - minPrice
            if potentialProfit > maxProfit:
                maxProfit = potentialProfit
        return maxProfit
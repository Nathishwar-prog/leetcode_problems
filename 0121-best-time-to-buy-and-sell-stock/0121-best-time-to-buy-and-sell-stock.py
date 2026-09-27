class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum_price = prices[0]
        maximum_profit = 0

        for price in prices:

            minimum_price = min(minimum_price, price)

            profit = price - minimum_price

            maximum_profit = max(maximum_profit, profit)

        return maximum_profit

        
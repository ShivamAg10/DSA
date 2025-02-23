class Solution:
    def maxProfit(self, prices) -> int:
        minPrice = prices[0]
        profit = 0

        for i in prices:
            if (i - minPrice) > profit:
                profit = i - minPrice
            if i < minPrice:
                minPrice = i
        return profit
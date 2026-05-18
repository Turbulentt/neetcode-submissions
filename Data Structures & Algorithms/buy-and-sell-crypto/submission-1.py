class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = prices[0]
        bestprofit = 0

        for x in prices:
           buyprice = min(buyprice, x)
           bestprofit = max(bestprofit, x - buyprice)

        return bestprofit
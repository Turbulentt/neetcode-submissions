class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = 101
        bestprofit = 0

        for x in prices:
            if x < buyprice:
                buyprice = x
            profit = x - buyprice
            if profit > bestprofit:
                bestprofit = profit

        return bestprofit
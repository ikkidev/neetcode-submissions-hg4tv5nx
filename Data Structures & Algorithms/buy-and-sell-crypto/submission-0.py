class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #B = buy day , S = sell day
        B = 0
        maxProfit = 0

        for S in range(1,len(prices)):
            if prices[S] > prices[B]:
                curProfit = prices[S] - prices[B]
                maxProfit = max(curProfit, maxProfit)
            
            else:
                B = S

        return maxProfit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0


        cur = 0
        i = 0
        for j, price in enumerate(prices):
            if price - prices[i] > cur:
                cur = price - prices[i]
            if price < prices[i]:
                i = j
        
        return cur

            



            


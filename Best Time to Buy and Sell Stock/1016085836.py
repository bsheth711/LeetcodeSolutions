class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0


        cur = 0
        i = 0
        for j, price in enumerate(prices):
            cur = (price - prices[i]) * (price - prices[i] > cur) + cur * (price - prices[i] <= cur)
            i = j * (price < prices[i]) + i * (price >= prices[i])
             
        return cur

            



            


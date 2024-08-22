class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        curBuy = sys.maxsize

        for price in prices:
            best = max(best, price - curBuy)
            curBuy = min(curBuy, price)
        
        return best

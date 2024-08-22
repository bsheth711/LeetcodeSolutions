class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        curBuy = sys.maxsize

        for price in prices:
            if price - curBuy > best:
                best = price - curBuy
            if price < curBuy:
                curBuy = price
        
        return best

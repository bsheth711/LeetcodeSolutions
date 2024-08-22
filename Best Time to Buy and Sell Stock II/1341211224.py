class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last = sys.maxsize
        profit = 0

        for price in prices:
            if last < price:
                profit += price - last
            last = price

        return profit
        
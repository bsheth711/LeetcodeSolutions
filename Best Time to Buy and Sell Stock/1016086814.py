class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0


        cur = 0
        minimum = sys.maxsize
        for price in prices:
            cur = (price - minimum) * (price - minimum > cur) + cur * (price - minimum <= cur)
            minimum = price * (price < minimum) + minimum * (price >= minimum)

        return cur

            



            


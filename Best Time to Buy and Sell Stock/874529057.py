class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # lets try kadane's algo

        curBest = 0
        curMin = sys.maxsize

        for price in prices:
            check = price - curMin

            if check > curBest:
                curBest = check 
            
            if price < curMin:
                curMin = price

        return curBest

            


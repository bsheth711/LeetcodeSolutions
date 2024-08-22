class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = end

        if len(piles) == h:
            return res
        
        while start <= end:
            mid = (start + end) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                res = mid
                end = mid - 1
            else:
                start = mid + 1

        return res
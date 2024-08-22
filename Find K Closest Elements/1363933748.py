class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # (-difference, value)
        pq = []
        worst = -1000000

        counter = 0
        for i in range(k):
            heappush(pq, (worst, -counter, 0))
            counter += 1


        for val in arr:
            heappushpop(pq, (-abs(val - x), -counter, val))
            counter += 1
        
        ls = [x[2] for x in pq]
        ls.sort()

        return ls


        

        
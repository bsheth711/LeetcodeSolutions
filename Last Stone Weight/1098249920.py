class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []

        for stone in stones:
            heappush(pq, -stone)
        
        while len(pq) > 1:
            x = heappop(pq)
            y = heappop(pq)

            z = -abs(x - y)

            if z != 0:
                heappush(pq, z)

        if pq:
            return abs(pq[0])
        
        return 0
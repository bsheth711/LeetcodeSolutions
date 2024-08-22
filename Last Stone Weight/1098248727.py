class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []

        for stone in stones:
            heappush(pq, (-stone, stone))
        
        while len(pq) > 1:
            x = heappop(pq)[1]
            y = heappop(pq)[1]

            z = abs(x - y)

            if z != 0:
                heappush(pq, (-z, z))

        if pq:
            return pq[0][1]
        
        return 0
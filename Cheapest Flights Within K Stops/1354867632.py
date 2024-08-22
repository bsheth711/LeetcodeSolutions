class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacent = defaultdict(list)

        for s, d, cost in flights:
            adjacent[s].append((cost, d))
        
        frontier = []
        visited = {}

        heapq.heappush(frontier, (0, 0, src))

        while frontier:
            curCost, numStops, curStop = heapq.heappop(frontier)
            if curStop == dst:
                return curCost

            if numStops > k:
                continue

            if curStop not in visited or visited[curStop] > numStops:
                visited[curStop] = numStops
                for nextCost, nextStop in adjacent[curStop]:
                        heapq.heappush(frontier, (curCost + nextCost, numStops + 1, nextStop))
        
        return -1





class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        pq = []
        costs = defaultdict(lambda: sys.maxsize)
        m = len(grid)
        n = len(grid[0])

        heappush(pq, (grid[0][0], (0, 0)))
        costs[(0, 0)] = grid[0][0]

        while pq:
            cost, (x, y) = heappop(pq)

            if x == m - 1 and y == n - 1:
                return cost

            if x + 1 < m:
                neighborCost = costs[(x, y)] + grid[x + 1][y]

                if neighborCost < costs[(x + 1, y)]:
                    costs[(x + 1, y)] = neighborCost
                    heappush(pq, (neighborCost, (x + 1, y)))
            
            if y + 1 < n:
                neighborCost = costs[(x, y)] + grid[x][y + 1]

                if neighborCost < costs[(x, y + 1)]:
                    costs[(x, y + 1)] = neighborCost
                    heappush(pq, (neighborCost, (x, y + 1)))

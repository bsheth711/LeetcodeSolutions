class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (distance, point)
        pq = []

        for point in points:

            if len(pq) < k:
                heappush(pq, (-(point[0] ** 2 + point[1] ** 2), point))
            else:
                heappushpop(pq, (-(point[0] ** 2 + point[1] ** 2), point))      
        
        res = [] 
        for point in pq:
            res.append(point[1])
        
        return res
            






        
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        processedPoints = []

        for tag, (x, y) in zip(s, points):
            processedPoints.append((max(abs(x), abs(y)), tag))
        
        processedPoints.sort()

        pointsInSquare = set()
        lengths = defaultdict(int)

        for length, tag in processedPoints:
            if tag in pointsInSquare:
                return len(pointsInSquare) - lengths[length]

            lengths[length] += 1
            pointsInSquare.add(tag)
        
        return len(pointsInSquare)
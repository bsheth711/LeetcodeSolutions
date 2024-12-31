class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        distances = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)]

        distances.sort()

        if distances[0] == 0:
            return False

        for i in range(4):
            if distances[0] != distances[i]:
                return False
        
        if distances[-1] != distances[-2]:
            return False

        return True

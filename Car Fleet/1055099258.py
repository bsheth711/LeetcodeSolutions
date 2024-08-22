class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        fleets = 0
        curTime = 0
        for p, s in pair:
            newTime = (target - p) / s

            if newTime > curTime:
                fleets += 1
                curTime = newTime
        
        return fleets
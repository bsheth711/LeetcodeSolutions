class Solution:
    def canJump(self, nums: List[int]) -> bool:
        airTime = 0

        for potentialAirTime in nums:
            if airTime < 0:
                return False

            if potentialAirTime > airTime:
                airTime = potentialAirTime
            
            airTime -= 1

        return True
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        airTime = 0

        for num in nums:
            if airTime < 0:
                return False

            airTime = max(airTime, num)
            
            airTime -= 1

        return True
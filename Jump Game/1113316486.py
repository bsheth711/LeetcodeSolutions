class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0

        for num in nums:
            if cur < 0:
                return False

            if num > cur:
                cur = num
            
            cur -= 1

        
        return True
        
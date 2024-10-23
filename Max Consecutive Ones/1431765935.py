class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curBest = 0
        cur = 0

        for num in nums:
            if num == 1:
                cur += 1
                curBest = max(curBest, cur)
            else:
                cur = 0
        
        return curBest
        
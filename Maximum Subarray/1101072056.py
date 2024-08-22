class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = -inf

        for num in nums:
            cur = max(num, num + cur)
            best = max(best, cur)
        
        return best
        
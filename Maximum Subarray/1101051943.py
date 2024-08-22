class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = -inf

        for num in nums:
            if cur + num >= num:
                cur = cur + num
            else:
                cur = num
            #cur = max(num, cur + num)
            best = max(best, cur)

        return best
        
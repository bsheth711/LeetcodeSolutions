class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur = 0
        best = 0
        prev = float('-inf')

        for num in nums:
            if num > prev:
                cur += 1
                best = max(cur, best)
            else:
                cur = 1
            
            prev = num

        return best
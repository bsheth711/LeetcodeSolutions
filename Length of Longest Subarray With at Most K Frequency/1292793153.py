class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        best = 0
        i = 0

        for j, num in enumerate(nums):
            counts[num] += 1

            # increment i
            while counts[num] > k:
                counts[nums[i]] -= 1
                i += 1
                
            best = max(best, j - i + 1)
        
        return best



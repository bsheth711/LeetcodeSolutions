class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        best = 0

        i = 0
        j = 0

        while j < len(nums):
            counts[nums[j]] += 1

            # increment i
            while counts[nums[j]] > k:
                counts[nums[i]] -= 1
                if counts[nums[i]] <= 0:
                    del counts[nums[i]]
                
                i += 1
                
            best = max(best, j - i + 1)
            j += 1
        
        return best



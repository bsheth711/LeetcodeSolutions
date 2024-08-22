class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(lambda: 0)
        best = 0
        cur = 0

        i = 0
        j = 0

        while j < len(nums):
            counts[nums[j]] += 1
            cur += 1

            # increment i
            while counts[nums[j]] > k:
                counts[nums[i]] -= 1
                if counts[nums[i]] <= 0:
                    del counts[nums[i]]
                
                cur -= 1
                i += 1
                
            best = max(best, cur)
            j += 1
        
        return best



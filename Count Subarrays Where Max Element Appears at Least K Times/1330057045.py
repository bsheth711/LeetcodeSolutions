class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        res = 0
        best = max(nums)
        curCount = 0

        for end in range(len(nums)):
            if nums[end] == best:
                curCount += 1
            while curCount == k:
                if nums[start] == best:
                    curCount -= 1
                start += 1
            res += start

        return res
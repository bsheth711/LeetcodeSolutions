class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = len(nums) - 1
        end = 0

        startHeap = []
        endHeap = []

        for i in range(len(nums)): 
            rev = len(nums) - i - 1

            while startHeap and nums[startHeap[-1]] > nums[i]:
                start = min(start, startHeap.pop())
            startHeap.append(i)

            while endHeap and nums[endHeap[-1]] < nums[rev]:
                end = max(end, endHeap.pop())
            endHeap.append(rev)
        
        if start >= end:
            return 0
        
        return end - start + 1



       

        
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        start = 0

        for a, b in zip(sortedNums, nums):
            if a != b:
                break
            start += 1

        end = len(nums) - 1

        if start == len(nums):
            return 0 

        for a, b in zip(reversed(sortedNums), reversed(nums)):
            if a != b:
                break
            end -= 1
        
        return end - start + 1

        
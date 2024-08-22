class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in numbers:
            if num-1 not in numbers:
                run = 1
    
                while (num + run) in numbers:
                    run += 1
    
                longest = max(longest, run)
            
       
        return longest
            

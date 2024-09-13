class Solution:
    '''
    Similar to max subarray sum problem, please look at the notes in that problem for KADANE'S ALGO intuition
    '''
    def maxProduct(self, nums: List[int]) -> int:
        maxSoFar = float('-inf')
        prefix = 0
        suffix = 0
        n = len(nums)

        for i in range(len(nums)):
            prefix *= nums[i] # compute product from left
            suffix *= nums[n-i-1] # compute product from right

            # When products fall to 0, then reset (KADANE'S algo)
            if prefix == 0:
                prefix = nums[i]

            if suffix == 0:
                suffix = nums[n-i-1] # this can be written as nums[~i] in python. REMEMBER THIS!
                
            maxSoFar = max(maxSoFar, prefix, suffix)
        
        return maxSoFar
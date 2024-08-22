class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        suffix = 1
        ans = [1]*len(nums)

        for i, num in enumerate(nums):
            ans[i] *= prefix
            prefix *= num
            ans[-1-i] *= suffix
            suffix *= nums[-1-i]
        
        return ans
        




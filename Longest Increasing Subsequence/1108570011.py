class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        L = [1] * len(nums)

        for i in range(1, len(nums)):
            subproblems = [L[k] for k in range(i) if nums[k] < nums[i]]
            if subproblems:
                L[i] = 1 + max(subproblems)
            else:
                L[i] = 1

        return max(L)
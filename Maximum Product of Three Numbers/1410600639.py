class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # could be reduced to O(n) from this O(nlogn) solution
        # but this solution may be faster due to the optimizations built in python
        # functions have for all but the largest n's
        nums.sort()

        top = nums[-1] * nums[-2] * nums[-3]
        mix = nums[0] * nums[1] * nums[-1]

        return max(top, mix)
        
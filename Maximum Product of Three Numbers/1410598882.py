class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        top = nums[-1] * nums[-2] * nums[-3]
        mix = nums[0] * nums[1] * nums[-1]

        return max(top, mix)
        
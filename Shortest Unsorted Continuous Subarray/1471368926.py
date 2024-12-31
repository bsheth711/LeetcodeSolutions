class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right = -1
        maximum = -1e6

        for i in range(len(nums)):
            if nums[i] >= maximum:
                maximum = nums[i]
            else:
                right = i

        left = len(nums)
        minimum = 1e6

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= minimum:
                minimum = nums[i]
            else:
                left = i

        return max(0, right - left + 1)
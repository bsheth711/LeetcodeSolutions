class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right = -1
        maximum = -1e6

        left = len(nums)
        minimum = 1e6

        for i in range(len(nums)):
            if nums[i] >= maximum:
                maximum = nums[i]
            else:
                right = i

            if nums[len(nums) - i - 1] <= minimum:
                minimum = nums[len(nums) - i - 1]
            else:
                left = len(nums) - i - 1

        return max(0, right - left + 1)
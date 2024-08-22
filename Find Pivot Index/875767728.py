class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left = 0
        right = sum(nums[1:])

        for i, num in enumerate(nums):
            if left == right:
                return i
 
            left += num

            if i != len(nums) - 1:
                right -= nums[i+1]
            else:
                right = 0

        return -1
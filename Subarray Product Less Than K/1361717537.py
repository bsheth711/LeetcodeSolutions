class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        i = 0
        j = 0
        product = 1
        numArrays = 0
        counter = 0

        while j < len(nums):
            product *= nums[j]

            while product >= k:
                product //= nums[i]
                i += 1

            numArrays += 1 + (j - i)
            j += 1

        return numArrays

        
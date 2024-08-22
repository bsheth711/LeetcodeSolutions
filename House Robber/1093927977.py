class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            x = 0
            if i-2 >= 0:
                x = nums[i-2]

            y = 0
            if i-3 >= 0:
                y = nums[i-3]

            nums[i] += max(x, y)
        
        return max(nums[-1], nums[-2])

        
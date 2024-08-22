class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0 

        while i < len(nums):
            if nums[i] == 0:
                j = i + 1

                while j < len(nums):
                    if nums[j] != 0: 
                        nums[i] = nums[j]
                        nums[j] = 0
                        break

                    if j == len(nums) - 1:
                        return
 
                    j += 1
       
            i += 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        first = True

        while j < len(nums) and i < len(nums):
            nums[i] = nums[j]

            if first:
                j += 1

                if j < len(nums) and nums[i] == nums[j]:
                    first = False
            else:
                while j < len(nums) and nums[i] == nums[j]:
                    j += 1
                
                first = True
            
            i += 1
        
        return i
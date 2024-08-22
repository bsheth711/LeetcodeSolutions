class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prevNum = -101

        i = 0
        while i < len(nums):

            if nums[i] == prevNum:
                nums.remove(nums[i])
                i -= 1
            else:
                prevNum = nums[i]

            i += 1
        
        return len(nums)
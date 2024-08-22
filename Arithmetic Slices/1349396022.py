class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        previousDifference = None
        sliceLength = 0
        total = 0

        for i in range(len(nums) - 1):
            currentDifference = nums[i] - nums[i + 1]
            
            if currentDifference == previousDifference:
                sliceLength += 1
            else:
                sliceLength = 0
            
            previousDifference = currentDifference
            total += sliceLength
        
        return total
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        prevDiff = None
        counter = 0
        total = 0
        for i in range(len(nums) - 1):
            diff = nums[i] - nums[i + 1]
            if diff == prevDiff:
                counter += 1
            else:
                prevDiff = diff
                counter = 0
            
            if counter > 0:
                total += counter
        
        return total
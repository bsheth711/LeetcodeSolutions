class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        nextPlace = 0

        for num in nums:
            if num != 0:
                nums[nextPlace] = num
                nextPlace += 1
            else:
                counter += 1

        for i in range(counter):
            nums[-i-1] = 0

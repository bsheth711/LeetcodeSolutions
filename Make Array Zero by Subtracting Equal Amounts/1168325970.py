class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        cur = 0
        counter = 0

        # [0, 0, 2, 4, 4]

        for num in nums:
            if cur < num:
                cur = num
                counter += 1 

        return counter
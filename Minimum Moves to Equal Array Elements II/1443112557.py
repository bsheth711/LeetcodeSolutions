class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        median = 0
        mid = len(nums) // 2

        if len(nums) % 2 == 0:
            median = (nums[mid] + nums[mid - 1]) // 2
        else:
            median = nums[mid]

        moves = 0

        for num in nums:
            moves += abs(num - median)

        return moves


        
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = [num ** 2 for num in nums]
        return sorted(ret)
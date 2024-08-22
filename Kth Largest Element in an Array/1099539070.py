class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new = sorted(nums) 
        return new[-k]
        
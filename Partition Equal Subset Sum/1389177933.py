class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False

        target = 1 << (total // 2)
        seen = 1
        for num in nums:
            seen |= seen << num
            if target & seen == target:
                return True
        return False
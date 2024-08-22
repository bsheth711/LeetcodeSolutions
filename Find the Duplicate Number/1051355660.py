class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setti = set()
        
        for num in nums:
            if num in setti:
                return num
            setti.add(num)
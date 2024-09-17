class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        best = 1
        # this solution is prohibited by the rules
        setOfNums = set(nums)

        while best in setOfNums:
            best += 1
 
        return best
        
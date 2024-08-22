class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        ranges.append([nums[0], nums[0]])
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num - 1 == ranges[-1][1]:
                ranges[-1][1] = num
            else:
                ranges.append([num, num])
        
        ret = []

        for r in ranges:
            if r[0] == r[1]:
                ret.append(str(r[0]))
            else:
                ret.append(f"{r[0]}->{r[1]}")
        
        return ret
        
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        powersOfTwo = [2**x for x in range(32)]
        counts = defaultdict(lambda: 0)

        for num in nums:
            for power in powersOfTwo:
                if (num & power) == power:
                    counts[power] += 1
        
        ret = 0
        for power in counts:
            if counts[power] >= k:
                ret += power
 
        return ret
        
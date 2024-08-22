class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums) 
        ls = []

        for num in counts:
            ls.append((counts[num], -num))
        
        ls.sort()

        ret = []
        for count, num in ls:
            for _ in range(count):
                ret.append(-num)

        return ret
    

        
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def cmpCounts(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            elif a[1] < b[1]:
                return 1
            elif a[1] > b[1]:
                return -1
            
            return 0

        counts = Counter(nums) 
        ls = []

        for num in counts:
            ls.append((counts[num], num))
        
        ls.sort(key=cmp_to_key(cmpCounts))

        ret = []
        for count, num in ls:
            for _ in range(count):
                ret.append(num)

        return ret
    

        
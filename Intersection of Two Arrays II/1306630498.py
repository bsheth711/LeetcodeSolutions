class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)
        counts1Set = set() 
        ret = []

        for num in nums1:
            counts1[num] += 1
            counts1Set.add(num)
        
        for num in nums2:
            if num in counts1Set:
                counts2[num] += 1
        
        for num in counts2:
            ret.extend([num] * (min(counts1[num], counts2[num])))
        
        return ret
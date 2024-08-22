class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ret = 0
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)

        for num in nums1:
            counts1[num] += 1
        
        for num in nums2:
            counts2[num * k] += 1
        
        for num1 in counts1:

            for i in range(1, floor(sqrt(num1)) + 1):
                if num1 % i != 0:
                    continue 
                ret += counts1[num1] * counts2[i]
                if i != num1 // i:
                    ret += counts1[num1] * counts2[num1 // i]

        return ret

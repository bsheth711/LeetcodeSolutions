class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i, target in enumerate(nums):
            hashtable = {}

            for j, num in enumerate(nums):
                if num in hashtable:
                    if i == j or i == hashtable[num] or j == hashtable[num]:
                        continue
                        
                    ls = [target, num, nums[hashtable[num]]]
                    ls.sort()
                    res.add(tuple(ls))

                hashtable[-target - num] = j
        
        return res
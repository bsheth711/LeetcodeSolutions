class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # return map(Counter, combinations_with_replacement(nums, len(nums)))

        res = [tuple()]
        total = set()

        for num in nums:

            toAdd = []

            for l in res:
                t = l + (num,)
                key = tuple(sorted(Counter(t).items())) # unique signature
                if key not in total:
                    total.add(key)
                    toAdd.append(t)
            
            res.extend(toAdd)
        
        return res


            
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        superSet = [[]]

        for num in nums:
            toAdd = []

            for s in superSet:
                new = s.copy()
                new.append(num)
                toAdd.append(new)
            
            superSet.extend(toAdd)
        
        return superSet
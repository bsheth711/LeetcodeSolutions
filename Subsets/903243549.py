class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = [[]]

        for num in nums:

            toAdd = []
            for entry in ls:
                tmp = entry.copy()
                tmp.append(num)
                toAdd.append(tmp)
            
            ls.extend(toAdd)
        
        return ls
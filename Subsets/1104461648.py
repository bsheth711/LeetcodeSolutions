class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]

        last = self.subsets(nums[:len(nums)-1])
        tmp = deepcopy(last)

        for entry in last:
            entry.append(nums[-1])
        
        last.extend(tmp)

        return last



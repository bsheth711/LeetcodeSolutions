class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        want = {}

        for i, num in enumerate(nums):
            var = want.get(num)

            if var != None:
                ans.append(var)
                ans.append(i)
                return ans
            
            want[target - num] = i


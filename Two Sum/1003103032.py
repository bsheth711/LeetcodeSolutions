class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()

        for i, num in enumerate(nums):
            if num in hashtable:
                return [i, hashtable[num]]

            hashtable[target - num] = i
        
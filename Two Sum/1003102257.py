class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        i = 0

        for num in nums:
            if num in hashtable:
                return [i, hashtable[num]]

            hashtable[target - num] = i
            i += 1
        
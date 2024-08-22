class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. binary search to find where numbers less than target end
        # 2. two pointers, 1 at top of region one at bottom of region
        #    if sum of elements at pointers is too large move right pointer left
        #    if sum of elements at pointers is too small move left pointer right

        i = 0
        j = len(numbers) - 1

        #while numbers[j] >

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return [i+1, j+1]
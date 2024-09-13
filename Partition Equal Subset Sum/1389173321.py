class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        values = set()
        values.add(0)

        for num in nums:

            toAdd = []

            for value in values:
                cur = num + value
                
                if cur == target:
                    return True
                
                toAdd.append(cur)
                
            values.update(toAdd)
        
        return False
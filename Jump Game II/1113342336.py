class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        cur = 0
        counter = 1

        while not (cur + nums[cur] >= len(nums) - 1):
            best = 0
            bestValue = 0

            for i in range(cur+1, min(len(nums), cur+nums[cur]+1)):
                if i + nums[i] > bestValue:
                    bestValue = i + nums[i]
                    best = i
            
            cur = best
            counter += 1
        
        return counter

        
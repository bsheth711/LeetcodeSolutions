class Solution:
    def jump(self, nums: List[int]) -> int:
        # 1, 1, 1, 4, 3, 49, 1
        if len(nums) <= 1:
            return 0
            
        cur = 0
        counter = 0

        while True:
            if cur + nums[cur] >= len(nums) - 1:
                counter += 1
                break
            
            best = 0
            bestValue = 0

            for i in range(cur+1, min(len(nums), cur+nums[cur]+1)):
                if i + nums[i] > bestValue:
                    bestValue = i + nums[i]
                    best = i
            
            cur = best
            counter += 1

        return counter

        
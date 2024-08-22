class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # greedy where we choose the jump with the best value each time where value is:
        cur = 0
        while True:
            if cur + nums[cur] >= len(nums) - 1:
                return True

            if nums[cur] <= 0:
                return False
            
            best = None
            bestValue = -inf
            
            #print('options:')
            for i in range(cur+1, cur + nums[cur]+1):
                #print(f'\t{nums[i]}')

                if i + nums[i] > bestValue:
                    bestValue = i + nums[i]
                    best = i

            if not best:
                return False
            
            cur = best

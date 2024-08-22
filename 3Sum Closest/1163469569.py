class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        s = sorted(nums)
        res = sum(s[:3])
        cur = res
        last = cur

        for i, num in enumerate(s):

            j = i + 1
            k = len(s) - 1

            while j < k:
                last = cur
                cur = num + s[j] + s[k]

                #if i != j and j != k and i != k:
                if abs(target - cur) < abs(target - res):
                    res = cur
                
                    if res == target:
                        return res
                
                if cur > target:
                    k -= 1
                else:
                    j += 1                
        
        return res
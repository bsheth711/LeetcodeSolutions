class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: -x)

        ret = 0 

        for i in range(len(nums) - 1):
            hypot = nums[i]

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    ret += k - j
                    j += 1
                else:
                    k -= 1
        
        return ret

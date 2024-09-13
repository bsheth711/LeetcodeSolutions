class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # modified Kadane's algorithm


        curBest = -(sys.maxsize - 1)
        options = [1]

        for num in nums:
            if num > 0:
                for i in range(len(options)):
                    options[i] *= num
                    curBest = max(curBest, options[i])
            elif num < 0:
                hasPositive = False
                
                for i in range(len(options)):
                    options[i] *= num
                    if options[i] > 0:
                        hasPositive = True
                    curBest = max(curBest, options[i])

                if not hasPositive:
                    options.append(1)
            else:
                options = [1]
                curBest = max(curBest, 0)

        return curBest
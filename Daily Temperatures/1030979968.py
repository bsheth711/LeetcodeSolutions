class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        stack.append((temperatures[0], 0))

        for i, temp in enumerate(temperatures[1:]):
            i += 1

            while len(stack) > 0 and temp > stack[-1][0]:
                cur = stack.pop()
                ans[cur[1]] = i - cur[1] 

            stack.append((temp, i))
        
        
        return ans
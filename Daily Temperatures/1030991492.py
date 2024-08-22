class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []


        for i, temp in enumerate(temperatures):

            while len(stack) > 0 and temp > temperatures[stack[-1]]:
                cur = stack.pop()
                ans[cur] = i - cur 

            stack.append(i)
        
        
        return ans
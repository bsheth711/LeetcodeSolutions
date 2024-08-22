class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(cur, curTotal, i):
            if curTotal == target:
                res.append(cur.copy())
                return
            if curTotal > target or i >= len(candidates):
                return
            


            cur.append(candidates[i])
            backtrack(cur, curTotal + candidates[i], i + 1)
    
            last = cur.pop()
            nextI = i + 1
            while nextI < len(candidates) and candidates[nextI] == last:
                nextI += 1
            
            backtrack(cur, curTotal, nextI) 
        
        backtrack([], 0, 0)
        return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return


            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            backtrack(cur, total + candidates[i], i)
            cur.pop()
            backtrack(cur, total, i+1)
        
        backtrack([], 0, 0)

        return res

            

        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curList, curTotal):
            if curTotal == target:
                res.append(curList[:])
                return
            if curTotal > target or i >= len(candidates):
                return


            curList.append(candidates[i])
            dfs(i, curList, curTotal + candidates[i])
            curList.pop()
            dfs(i + 1, curList, curTotal)
        
        dfs(0, [], 0)

        return res
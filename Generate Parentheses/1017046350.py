class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = ["("]
        counts = [(1, 0)]

        for i in range(2 * n - 1):
            nextCur = []
            nextCounts = []

            for j, branch in enumerate(cur):
                if counts[j][0] < n:
                    if counts[j][1] < counts[j][0]:
                        nextCur.append(branch + ")")
                        nextCounts.append((counts[j][0], counts[j][1] + 1))

                    nextCur.append(branch + "(")
                    nextCounts.append((counts[j][0] + 1, counts[j][1]))
                else: 
                    nextCur.append(branch + ")")
                    nextCounts.append((counts[j][0], counts[j][1] + 1))
            
            cur = nextCur
            counts = nextCounts
        
        return cur

            

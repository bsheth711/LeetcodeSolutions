class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        upwards = True
        i = 0
        j = 0

        ret = []

        while True:
            ret.append(mat[i][j])

            if i == m - 1 and j == n - 1:
                break

            if upwards:
                i -= 1
                j += 1

                # if out of bounds, move right, otherwise below
                if i < 0 or j >= n:  
                    i += 1

                    if i < 0 or j >= n:
                        i += 1
                        j -= 1

                    upwards = False
                    
            else:
                i += 1
                j -= 1

                # if out of bounds, move below, otherwise right
                if i >= m or j < 0:
                    j += 1

                    if i >= m or j < 0:
                        i -= 1
                        j += 1
                    
                    upwards = True
            

        return ret







        
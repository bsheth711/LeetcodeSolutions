class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        upwards = True
        i = 0
        j = 0

        ret = []

        for _ in range(m * n):
            ret.append(mat[i][j])

            if upwards:
                i -= 1
                j += 1

                # bounds check, move right of previous square
                if i < 0 or j >= n:  
                    i += 1

                    # bounds check, move below previous square
                    if i < 0 or j >= n:
                        i += 1
                        j -= 1

                    upwards = False
                    
            else:
                i += 1
                j -= 1

                # bounds check, move below of previous square
                if i >= m or j < 0:
                    j += 1

                    # bounds check, move right of previous square
                    if i >= m or j < 0:
                        i -= 1
                        j += 1
                    
                    upwards = True
            
        return ret
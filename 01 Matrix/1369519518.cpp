class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int tmp = m + n;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] != 0) {
                    mat[i][j] = tmp;
                }
            }
        } 

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                
                if (mat[i][j] != 0) {

                    int top = (i - 1 >= 0) ? mat[i - 1][j] : tmp;
                    int left = (j - 1 >= 0) ? mat[i][j - 1] : tmp;

                    mat[i][j] = min(mat[i][j], min(top, left) + 1);
                } 

                int x = m - i - 1;
                int y = n - j - 1;

                if (mat[x][y] != 0) {

                    int top = (x - 1 >= 0) ? mat[x - 1][y] : tmp;
                    int left = (y - 1 >= 0) ? mat[x][y - 1] : tmp;

                    int topOrLeft = min(top, left);

                    int bottom = (x + 1 < m) ? mat[x + 1][y] : tmp;
                    int right = (y + 1 < n) ? mat[x][y + 1] : tmp;

                    int bottomOrRight = min(bottom, right);

    
                    mat[x][y] = min(mat[x][y], min(topOrLeft, bottomOrRight) + 1);
                }
            }
        }        

       
        return mat;
    }
};
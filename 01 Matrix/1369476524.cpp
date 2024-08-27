class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int tmp = 1000000;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] != 0) {
                    mat[i][j] = tmp;
                }
            }
        } 

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 0) {
                    continue;
                }
                
                int best = mat[i][j];
                if (i - 1 >= 0 && mat[i - 1][j] < best) {
                    best = mat[i - 1][j];
                }
                if (j - 1 >= 0 && mat[i][j - 1] < best) {
                    best = mat[i][j - 1];
                }

                mat[i][j] = min(mat[i][j], best + 1);
            }
        }

        
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (mat[i][j] == 0) {
                    continue;
                }
                
                int best = mat[i][j];
                if (i + 1 < m && mat[i + 1][j] < best) {
                    best = mat[i + 1][j];
                }
                if (i - 1 >= 0 && mat[i - 1][j] < best) {
                    best = mat[i - 1][j];
                }
                if (j + 1 < n && mat[i][j + 1] < best) {
                    best = mat[i][j + 1];
                }
                if (j - 1 >= 0 && mat[i][j - 1] < best) {
                    best = mat[i][j - 1];
                }

                mat[i][j] = min(mat[i][j], best + 1);
            }
        
        }
        


        return mat;



    }
};
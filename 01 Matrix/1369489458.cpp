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
                if (mat[i][j] != 0) {

                    int best = mat[i][j];

                    if (i - 1 >= 0 && mat[i - 1][j] < best) {
                        best = mat[i - 1][j];
                    }
                    if (j - 1 >= 0 && mat[i][j - 1] < best) {
                        best = mat[i][j - 1];
                    }
    
                    mat[i][j] = min(mat[i][j], best + 1);
                } 

                int x = m - i - 1;
                int y = n - j - 1;

                cout << i << " " << j << endl;
                cout << x << " " << y << endl;
                cout << endl;

                if (mat[x][y] != 0) {

                    int best = mat[x][y];
                    if (x + 1 < m && mat[x + 1][y] < best) {
                        best = mat[x + 1][y];
                    }
                    if (x - 1 >= 0 && mat[x - 1][y] < best) {
                        best = mat[x - 1][y];
                    }
                    if (y + 1 < n && mat[x][y + 1] < best) {
                        best = mat[x][y + 1];
                    }
                    if (y - 1 >= 0 && mat[x][y - 1] < best) {
                        best = mat[x][y - 1];
                    }                 
    
                    mat[x][y] = min(mat[x][y], best + 1);
                }
            }
        }        

       
        return mat;

    }
};
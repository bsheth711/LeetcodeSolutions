class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int start = 0;
        int end = matrix.size() * matrix[0].size();
        int length = end;

        /*
        if (matrix.size() == 1) {
            while (true) {
                int i = (end + start) / 2;

                if (i >= matrix[0].size()) {
                    break;
                }
    
                if (matrix[0][i] == target) {
                    return true;
                }
                else if (start >= end) {
                    break;  
                }
                else if (matrix[0][i] < target) {
                    start = i + 1;
                }
                else if (matrix[0][i] > target) {
                    end = i - 1;
                }
    
            } 

            return false;
        }
        */

        while (true) {
            //int i = ((end - start) / 2) + start;
            int i = (end + start) / 2;

            if (i >= length || i < 0) {
                break;
            }

            // translate i to 2D

            int x = i / matrix[0].size();
            int y = i % matrix[0].size();

            cout << "l: " << length << endl;
            cout << "i: " << i << endl;
            cout << "x: " << x << endl;
            cout << "y: " << y << endl;
            cout << "s: " << start << endl;
            cout << "e: " << end << endl;

            if (matrix[x][y] == target) {
                return true;
            }
            else if (start >= end) {
                break;  
            }
            else if (matrix[x][y] < target) {
                start = i + 1;
            }
            else if (matrix[x][y] > target) {
                end = i - 1;
            }

        }
        

        return false;
    }
};
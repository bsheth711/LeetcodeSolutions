class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int start = 0;
        int end = matrix.size() * matrix[0].size();
        int length = end;

        while (true) {
            //int i = ((end - start) / 2) + start;
            int i = (end + start) / 2;
            
            if (i >= length || i < 0) {
                break;
            }

            // translate i to 2D

            int x = i / matrix[0].size();
            int y = i % matrix[0].size();

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
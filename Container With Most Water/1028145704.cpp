class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1; 
        int curMax = 0;
        int area;

        while (i < j) {
            int num1 = height[i];
            int num2 = height[j];

            area = ((num1 < num2) * num1 + (num1 >= num2) * num2) * (j - i);

            if (num1 < num2) {
                i++;
            }
            else {
                j--;
            } 

            curMax = (area > curMax) * area + (area <= curMax) * curMax;
        }

        return curMax;
    }
};
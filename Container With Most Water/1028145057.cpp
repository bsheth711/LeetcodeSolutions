class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1; 
        int curMax = 0;
        int area;

        while (i < j) {

            area = ((height[i] < height[j]) * height[i] + (height[i] >= height[j]) * height[j] ) * (j - i);

            if (height[i] < height[j]) {
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
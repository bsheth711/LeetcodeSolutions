class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int previousDifference = -1001;
        int sliceLength = 0;
        int total = 0;

        for (int i = 0; i < nums.size() - 1; ++i) {
            int currentDifference = nums[i] - nums[i + 1];

            sliceLength = (currentDifference == previousDifference) * (sliceLength + 1);
            
            total += sliceLength;
            previousDifference = currentDifference;
        } 

        return total;
    }
};
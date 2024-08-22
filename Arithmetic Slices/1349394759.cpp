class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int previousDifference = -1001;
        int sliceLength = 0;
        int total = 0;

        for (int i = 0; i < nums.size() - 1; ++i) {
            int currentDifference = nums[i] - nums[i + 1];

            if (currentDifference == previousDifference) {
                ++sliceLength;
            }
            else {
                sliceLength = 0;
            }

            total += sliceLength;
            previousDifference = currentDifference;
        } 

        return total;
    }
};

/*
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        previousDifference = None
        sliceLength = 0
        total = 0

        for i in range(len(nums) - 1):
            currentDifference = nums[i] - nums[i + 1]
            
            if currentDifference == previousDifference:
                sliceLength += 1
            else:
                sliceLength = 0
            
            previousDifference = currentDifference
            total += sliceLength
        
        return total
*/
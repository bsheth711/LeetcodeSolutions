class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;

        while (true) {
            int i = (end + start) / 2;

            if (nums[i] == target) {
                return i;
            }
            else if (start >= end) {
                break;  
            }
            else if (nums[i] < target) {
                start = i + 1;
            }
            else if (nums[i] > target) {
                end = i - 1;
            }

        }

        return -1;
    }
};
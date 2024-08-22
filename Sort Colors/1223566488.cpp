class Solution {
public:
    void sortColors(vector<int>& nums) {
        map<int, int> counts;
        counts[0] = 0;
        counts[1] = 0;
        counts[2] = 0;


        for (const int& num : nums) {
            ++counts[num];
        }

        int counter = 0;
        for (auto& [key, value] : counts) {
            while (value > 0) {
                nums[counter] = key;
                --value;
                ++counter;
            }
        }
    }
};
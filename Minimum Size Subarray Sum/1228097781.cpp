class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0;
        int r = 0;
        int cur = 0;
        int best = INT_MAX;

        while ((l < nums.size()) && (r <= nums.size())) {
            // expand right
            if (cur < target) {
                if (r >= nums.size()) {
                    break;
                }
                cur += nums[r];
                ++r;
            }
            // cur >= target
            // contract left
            else {
                best = min(best, r - l);
                cur -= nums[l];
                ++l;
            }
        }

        if (best == INT_MAX) {
            return 0;
        }

        return best;
    }
};
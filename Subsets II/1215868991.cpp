class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        vector<int> cur;
        vector<vector<int>> res;

        helper(nums, cur, 0, res);

        return res;
    }

private:
    void helper(vector<int>& nums, vector<int>& cur, int idx, vector<vector<int>>& res) {
        if (idx == nums.size()) {
            res.push_back(vector<int>(cur));
            return;
        }
        else if (idx > nums.size()) {
            return;
        }

        cur.push_back(nums[idx]);

        helper(nums, cur, idx + 1, res);


        int last = nums[idx];

        while (idx < nums.size() && nums[idx] == last) {
            ++idx;
        }


        cur.pop_back();

        helper(nums, cur, idx ,res);
    }
};
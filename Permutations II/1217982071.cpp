class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        deque<int> dq(nums.begin(), nums.end());
        vector<int> cur;
        vector<vector<int>> res;
        dfs(dq, res, cur, nums.size());
        return res;
    }

private:
    void dfs(deque<int>& dq, vector<vector<int>>& res, vector<int>& cur, int target) {
        if (cur.size() == target) {
            res.push_back(vector<int>(cur));
            return;
        }

        int counter = 0;
        int dqSize = dq.size();
        while (counter < dqSize) {
            int curNum = dq.front();
            dq.pop_front();
            cur.push_back(curNum);
    
            dfs(dq, res, cur, target);
    
            cur.pop_back();
            dq.push_back(curNum);

            // cycle dq
            while (counter < dqSize && dq.front() == curNum) {
                int tmp = dq.front();
                dq.pop_front();
                dq.push_back(tmp);
                ++counter;
            }
            
            ++counter;
        }
    }
};
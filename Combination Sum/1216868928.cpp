class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> cur; 
        dfs(candidates, target, 0, 0, cur, res);
        return res;
    }

private:
    void dfs(vector<int>& candidates, int target, int curTotal, int idx, vector<int>& cur, vector<vector<int>>& res) {
        if (curTotal == target) {
            res.push_back(vector<int>(cur));
            return;
        }
        else if (curTotal > target || idx >= candidates.size()) {
            return;
        }

        cur.push_back(candidates[idx]);
        dfs(candidates, target, curTotal + candidates[idx], idx, cur, res);
        cur.pop_back();
        dfs(candidates, target, curTotal, idx + 1, cur, res);
    }
};
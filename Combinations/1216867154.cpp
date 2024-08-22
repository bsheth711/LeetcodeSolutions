class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> candidates(n);
        iota(candidates.begin(), candidates.end(), 1);
        vector<vector<int>> res;
        vector<int> cur;
        dfs(candidates, k, 0, 0, res, cur);
        return res;
    }
private:

    void dfs(const vector<int>& candidates, int k, int curLen, int i, vector<vector<int>>& res, vector<int>& cur) {
        if (curLen == k) {
            res.push_back(vector<int>(cur));
            return;
        }
        else if (curLen > k || i >= candidates.size()) {
            return;
        }

        cur.push_back(candidates[i]);
        dfs(candidates, k, curLen + 1, i + 1, res, cur);
        cur.pop_back();
        dfs(candidates, k, curLen, i + 1, res, cur);
    }
};
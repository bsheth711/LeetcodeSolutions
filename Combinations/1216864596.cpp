class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> candidates(n);
        iota(candidates.begin(), candidates.end(), 1);
        dfs(candidates, k, 0, 0);
        return res;
    }
private:
    vector<vector<int>> res;
    vector<int> cur;

    void dfs(const vector<int>& candidates, int k, int curLen, int i) {
        if (curLen == k) {
            res.push_back(vector<int>(cur));
            return;
        }
        else if (curLen > k || i >= candidates.size()) {
            return;
        }

        cur.push_back(candidates[i]);
        dfs(candidates, k, curLen + 1, i + 1);
        cur.pop_back();
        dfs(candidates, k, curLen, i + 1);
    }
};
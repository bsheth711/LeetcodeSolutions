class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, 0, 0);
        return res;
    }

private:
    vector<vector<int>> res;
    vector<int> cur; 

    void dfs(vector<int>& candidates, int target, int curTotal, int idx) {
        for (int elem : cur) {
            cout << elem << " ";
        }
        cout << endl;

        if (curTotal == target) {
            res.push_back(vector<int>(cur));
            return;
        }
        else if (curTotal > target || idx >= candidates.size()) {
            return;
        }

        cur.push_back(candidates[idx]);
        dfs(candidates, target, curTotal + candidates[idx], idx);
        cur.pop_back();
        dfs(candidates, target, curTotal, idx + 1);
    }
};
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        deque<int> dq(nums.begin(), nums.end());
        vector<int> cur;
        vector<vector<int>> res;
        unordered_map<int, int> counts;

        for (const int n : nums) {
            if (counts.contains(n)) {
                counts[n] += 1;
            }
            else {
                counts[n] = 1;
            }
        }

        //dfs(dq, res, cur, nums.size(), counts);
        dfs(dq, res, cur, nums.size());
        return res;
    }

private:
    //void dfs(deque<int>& dq, vector<vector<int>>& res, vector<int>& cur, int target, unordered_map<int, int>& counts) {
    void dfs(deque<int>& dq, vector<vector<int>>& res, vector<int>& cur, int target) {
        if (cur.size() == target) {
            res.push_back(vector<int>(cur));
            return;
        }

        /*
        int maxi = 0;
        for (auto const& [key, val] : counts) {
            if (val != 0) {
                ++maxi;
            }
        }
        */
        int counter = 0;
        for (;;) {
            int curNum = dq.front();
            dq.pop_front();
            cur.push_back(curNum);
            //counts[curNum] -= 1;
    
            //dfs(dq, res, cur, target, counts);
            dfs(dq, res, cur, target);
    
            cur.pop_back();
            dq.push_back(curNum);
            //counts[curNum] += 1;

            // cycle dq
            while (counter < dq.size() && dq.front() == curNum) {
                int tmp = dq.front();
                dq.pop_front();
                dq.push_back(tmp);
                ++counter;
            }
            
            ++counter;

            if (counter >= dq.size()) {
                break;
            }
        }

        /*
        for (int i = 0; i < dq.size(); ++i) {
            int curNum = dq.front();
            dq.pop_front();
            cur.push_back(curNum);
            //counts[curNum] -= 1;
    
            //dfs(dq, res, cur, target, counts);
            dfs(dq, res, cur, target);
    
            cur.pop_back();
            dq.push_back(curNum);
            //counts[curNum] += 1;

            // cycle dq
            int counter = 0;
            while (counter < dq.size() && dq.front() == curNum) {
                int tmp = dq.front();
                dq.pop_front();
                dq.push_back(tmp);
                ++counter;
            }
        }
        */

    }
};
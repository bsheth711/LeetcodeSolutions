class Solution {
public:
    int maxDepth(string s) {
        int best = 0;
        int cur = 0;

        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                ++cur;
                best = max(best, cur);
            }
            else if (s[i] == ')') {
                --cur;
            }
        } 

        return best;
    }
};
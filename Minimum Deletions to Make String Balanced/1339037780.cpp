class Solution {
public:
    int minimumDeletions(string s) {
        int deletions = 0;
        int bCount = 0;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == 'a') {
                deletions = min(deletions + 1, bCount);
            }
            else {
                ++bCount;
            }
        }

        return deletions;
    }
};
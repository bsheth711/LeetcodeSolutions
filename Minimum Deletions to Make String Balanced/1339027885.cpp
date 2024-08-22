class Solution {
public:
    int minimumDeletions(string s) {
        vector<int> dp(s.size() + 1, 0);
        int bCount = 0;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == 'a') {
                dp[i + 1] = min(dp[i] + 1, bCount);
            }
            else {
                dp[i + 1] = dp[i];
                ++bCount;
            }
        }

        return dp[s.size()];
    }
};

/**
--x---x-
aababbab
00011122


--x-xx-x---
aababbabaaa
00011122344

question: is b's in left greater than a's to right

*/
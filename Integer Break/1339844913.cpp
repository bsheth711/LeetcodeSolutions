class Solution {
public:
    int integerBreak(int n) {
        vector<int> dp(max(n + 3, 8), 0);
        dp[2] = 1;
        dp[3] = 2;
        dp[4] = 4;
        dp[5] = 6;
        dp[6] = 9;
        dp[7] = 12;

        for (int i = 8; i <= n; ++i) {
            if ((i - 1) % 3 == 0) {
                cout << "i: " << i << endl;
                dp[i] = dp[i - 1] + dp[i - 4];
            }
            else {
                dp[i] = dp[i - 1] + dp[i - 3];
            }
        }

        return dp[n];
    }
};

/**
n = 2

*/
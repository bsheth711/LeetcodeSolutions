class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> minCoins(amount + 1);

        sort(begin(coins), end(coins));

        minCoins[0] = 0;

        for (int i = 1; i < amount + 1; ++i) {
            int best = INT_MAX;

            for (const int& coin: coins) {
                if (i - coin < 0) {
                    break;
                }

                if (minCoins[i - coin] == -1) {
                    continue; 
                }

                best = min(best, 1 + minCoins[i - coin]);
            }

            minCoins[i] = best != INT_MAX ? best : -1;
        } 

        return minCoins[amount];
    }
};
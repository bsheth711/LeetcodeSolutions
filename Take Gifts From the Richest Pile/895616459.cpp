class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> piles {less<int>(), gifts};

        for (int i = 0; i < k; ++i) {
            piles.push((int) sqrt(piles.top()));
            piles.pop();
        }

        long long sum = 0;
        while (!piles.empty()) {
            sum += piles.top();
            piles.pop();
        }

        return sum;
    }
};
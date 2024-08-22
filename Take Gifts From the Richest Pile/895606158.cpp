class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        for (int i = 0; i < k; ++i) {

            int argmax = 0;
            for (int j = 0; j < gifts.size(); ++j) {
                if (gifts[argmax] < gifts[j]) {
                    argmax = j;
                }
            }

            gifts[argmax] = (int) sqrt(gifts[argmax]);
        }

        long long sum = 0;
        for (int pile : gifts) {
            sum += pile;
        }

        return sum;
    }
};
class Solution {
public:
    int minimumDeletions(string s) {
        pair<int, int> counts[s.size()];

        int counter = 0;
        for (int i = 0; i < s.size(); ++i) {
            counts[i].first = counter;
            if (s[i] == 'b') {
                counter += 1;
            }
        }

        counter = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            counts[i].second = counter;
            if (s[i] == 'a') {
                counter += 1;
            }
        }

        int best = INT_MAX;
        for (auto n : counts) {
            best = min(best, n.first + n.second);
        }

        return best;
    }
};

/**
--x---x-
aababbab
00011122


--x-xx-x---
aababbabaaa
0001

question: is b's in left greater than a's to right

*/
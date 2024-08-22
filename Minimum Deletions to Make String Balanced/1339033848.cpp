class Solution {
public:
    int minimumDeletions(string s) {
        int deletions = 0;
        int bCount = 0;

        for (int i = 0; i < s.size(); ++i) {
            bool isA = (s[i] == 'a');
            deletions = isA * min(deletions + 1, bCount) + !isA * deletions;
            bCount = isA * bCount + !isA * (bCount + 1);
        }

        return deletions;
    }
};
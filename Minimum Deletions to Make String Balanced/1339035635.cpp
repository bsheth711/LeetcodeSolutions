class Solution {
public:
    int minimumDeletions(string s) {
        int deletions = 0;
        int bCount = 0;

        for (int i = 0; i < s.size(); ++i) {
            bool isA = (s[i] == 'a');
            bool lessDeletions = (deletions + 1 < bCount);
            int lesser = lessDeletions * (deletions + 1) + !lessDeletions * (bCount);
            deletions = isA * lesser + !isA * deletions;
            bCount = isA * bCount + !isA * (bCount + 1);
        }

        return deletions;
    }
};
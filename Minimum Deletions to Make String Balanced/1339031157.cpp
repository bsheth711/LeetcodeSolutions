class Solution {
public:
    int minimumDeletions(string s) {
        int deletions = 0;
        int bCount = 0;

        for (int i = 0; i < s.size(); ++i) {
            deletions = (s[i] == 'a') * (min(deletions + 1, bCount)) + (s[i] != 'a') * (deletions);
            bCount = (s[i] == 'b') * (bCount + 1) + (s[i] != 'b') * (bCount);
        }

        return deletions;
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
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> hashtable = *(new unordered_map<char,int>());
        int max = 0;
        int start = 0;

        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];

            if (hashtable.count(c) > 0) {
                if (i - start > max) {
                    max = i - start;
                }

                if (start < hashtable[c] + 1) {
                    start = hashtable[c] + 1;
                }

            }
            
            hashtable[c] = i;

        }

        if (s.length() - start > max) {
            max = s.length() - start;
        }

        return max;
    }
};
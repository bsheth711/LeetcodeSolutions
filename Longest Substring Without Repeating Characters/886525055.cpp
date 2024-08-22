class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> hashtable = *(new unordered_map<char,int>());
        int max = 0;
        int start = 0;

        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];

            /*
            for (auto &pair : hashtable) {
                cout << "key: " << pair.first << " val: " << pair.second << "   ";
            }
            cout << "\n";
            
            for (int j = start; j < i; ++j) {
                cout << s[j];
            }
            cout << "\n";
            cout << "start: " << start << "\n";
            */

            if (hashtable.count(c) > 0) {
                if (i - start > max) {
                    max = i - start;
                }

                if (start < hashtable[c] + 1) {
                    start = hashtable[c] + 1;
                }

                hashtable[c] = i;
            }
            else {
                hashtable.insert({c, i});
            }

        }

        /*
        for (auto &pair : hashtable) {
            cout << "key: " << pair.first << " val: " << pair.second << "   ";
        }
        cout << "\n";
        for (int j = start; j < s.length(); ++j) {
            cout << s[j];
        }
        cout << "\n";
        cout << "start: " << start << "\n";
        */


        if (s.length() - start > max) {
            max = s.length() - start;
        }

        return max;
    }
};
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> chars;

        for (char c : s) {
            if (chars.count(c) > 0) {
                ++chars[c];
            }
            else {
                chars.insert({c, 1});
            }
        }

        for (char c : t) {
            if (chars.count(c) > 0) {
                if (chars[c] == 1) {
                    chars.erase(c);
                }
                else {
                    --chars[c];
                }
            }
            else {
                return false;
            }
        }

        if (chars.size() > 0) {
            return false;
        }

        return true;
    }
};
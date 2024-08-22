class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int best = -1;

        unordered_map<char, int> map;

        for (int i = 0; i < s.length(); ++i) {
            if (map.contains(s[i])) {
                best = max(i - map[s[i]] - 1, best);
            }
            else {
                map[s[i]] = i;
            }
        }

        return best;
    }
};
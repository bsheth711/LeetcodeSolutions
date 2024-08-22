class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1;
        int len = 0;
        bool started = false;

        while (i >= 0) {
            if (started) {
                if (s[i] == ' ') {
                    break; 
                }
                ++len;
            }
            else {
                if (s[i] != ' ') {
                    started = true; 
                    ++len;
                }
            }

            i -= 1;
        }

        return len;
        
    }
};
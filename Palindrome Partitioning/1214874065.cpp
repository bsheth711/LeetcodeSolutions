class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> pars;
        vector<string> par;
        partition(s, 0, par, pars);
        return pars;
    }
private:
    void partition(string& s, int cur, vector<string>& par, vector<vector<string>>& pars) {

        if (cur == s.length()) {
            pars.push_back(par);
        }
        else {
            for (int i = cur; i < s.length(); ++i) {
                if (isPalindrome(s, cur, i)) {
                    par.push_back(s.substr(cur, i - cur + 1));
                    partition(s, i + 1, par, pars);
                    par.pop_back();
                }
            }
        }
    }

    bool isPalindrome(const string& s, int i, int j) {
        while (i < j) {
            if (s[i++] != s[j--]) {
                return false;
            }
        }

        return true;
    }
};
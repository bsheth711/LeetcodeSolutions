class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> numbers;
        
        for (int num : nums) {
            if (numbers.count(num) > 0) {
                return true;
            }
            numbers.insert(num);
        }

        return false;
    }
};
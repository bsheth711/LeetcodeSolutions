class Solution {
    public int reverse(int x) {
        int sol = 0;
        int multiplier = 1;
        
        for (int temp = x; temp / 10 != 0; temp /= 10) {
            multiplier *= 10;
        }
        
        while (x != 0) {

            sol += x % 10 * multiplier;
            if (multiplier != 1) {
                if (sol % multiplier != 0) {
                    return 0;
                }
            }
            x /= 10;
            multiplier /= 10;
            
        }
        
        return sol;
    }
}
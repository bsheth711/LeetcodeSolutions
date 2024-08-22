class Solution {
    public int reverse(int x) {
        int sol = 0; 
        //int multiplier = 1; 
        
        /*
        for (int temp = x; temp / 10 != 0; temp /= 10) {
            multiplier *= 10;
        }
        */
        
        while (x != 0) {
            sol += x % 10;
            int checker = sol;
            
            /*
            if (sol % multiplier != 0) {
                return 0;
            }
            
            
            multiplier /= 10;
            */
            
            x /= 10;
            
            if (x != 0) {
                sol *= 10;
                if (sol / 10 != checker) {          
                    return 0;
                }
            }
            
        }
        
        return sol;
    }
}
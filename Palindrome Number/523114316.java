class Solution {
    public boolean isPalindrome(int x) {
        int copy = x;
        int rev = 0;
        
        if (x < 0) {
            return false;
        }
        
        while (x != 0) {
            rev += x % 10;
            x /= 10;
            /*
            if (x == 0) {
                break;
            } 
            */
            if (x != 0) {
                rev *= 10;
            }
            
        }
        
        if (rev == copy) {
            return true;
        }
        return false;
    }
}
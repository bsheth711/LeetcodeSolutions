class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        s = s.toLowerCase();
        char[] arr = s.toCharArray();
        
        
        for (int i = 0; i < arr.length/2; ++i) {
            if (arr[i] != arr[arr.length - 1 - i]) {
                return false;
            }
        }
        
        return true;
    }
}
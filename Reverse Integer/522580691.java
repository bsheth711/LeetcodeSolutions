class Solution {
    public int reverse(int x) {
        String str = String.valueOf(x);
        boolean neg = false;
        
        if (str.contains("-")) {
            neg = true;
            str = str.split("-")[1];
        }
        
        char[] chars = str.toCharArray();
        
        for (int i = 0; i < chars.length / 2; ++i) {
            char temp = chars[i];
            chars[i] = chars[chars.length - 1 - i];
            chars[chars.length - 1 - i] = temp;
        }
        
        int sol = 0;
    
        try {
            sol = Integer.parseInt(new String(chars));
        }
        catch (java.lang.NumberFormatException e) {
            return 0;
        }
        
        if (neg) {
            sol = -sol;
        }
        
        return sol;
    }
}
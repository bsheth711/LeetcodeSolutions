bool isPalindrome(char* s){
    int counter = 0;
    int length = strlen(s); 
    char clean[length];
    
    for (int i = 0; i < length; ++i) {
        if (s[i] >= 65 && s[i] <= 90) {
            clean[counter] = s[i] + 32;
            ++counter;
        }
        else if ((s[i] >= 48 && s[i]<= 57) || (s[i] >= 97 && s[i] <= 122)) {
            clean[counter] = s[i];
            ++counter;
        }
    }
    
    for (int i = 0; i < (counter + 1)/2; ++i) {
        if (clean[i] != clean[counter - 1 - i]) {
            return false;
        }
    }

    return true;
}
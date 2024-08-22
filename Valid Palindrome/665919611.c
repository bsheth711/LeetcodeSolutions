bool isPalindrome(char* s){
    char* p2 = (s + strlen(s) - 1);
    
    while(true) {
        //printf("p1: %c, p2: %c\n", *p1, *p2);  
        if (p2 <= s) {
            return true;
        }
        if (!isalnum(*s)) {
            ++s;
            continue;
        }
        if (!isalnum(*p2)){
            --p2;
            continue;
        }
        if (tolower(*s) != tolower(*p2)) {
            return false;
        }
        ++s;
        --p2;
    }
}
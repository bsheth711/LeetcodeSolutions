bool isPalindrome(char* s){
    char* p1 = s;
    char* p2 = (s + strlen(s) - 1);
    
    while(true) {
        //printf("p1: %c, p2: %c\n", *p1, *p2);  
        if (p2 <= p1) {
            return true;
        }
        if (!isalnum(*p1)) {
            ++p1;
            continue;
        }
        if (!isalnum(*p2)){
            --p2;
            continue;
        }
        if (tolower(*p1) != tolower(*p2)) {
            return false;
        }
        ++p1;
        --p2;
    }
}
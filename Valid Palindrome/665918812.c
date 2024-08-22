bool isAlphanumeric(char* c) {
    if (*c >= 65 && *c <= 90) {
        *c = *c + 32;
        return true;
    }
    else if ((*c >= 48 && *c <= 57) || (*c >= 97 && *c <= 122)) {
        return true;
    }
    return false;

}

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
        
    /*
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
    */
}
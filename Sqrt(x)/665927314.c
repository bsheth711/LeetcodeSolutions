int mySqrt(int x){ 
    long long int i = 0;
    while (i*i < x) {
        ++i;
    }
    if (i*i > x) {
        --i;
    }
    return i;
}
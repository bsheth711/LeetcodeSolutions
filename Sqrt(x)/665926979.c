int mySqrt(int x){ 
    long long int i = 0;
    long long int j = i + 1;
    while (i*i < x) {
        if (i*i - j * j > i * i - x) {
        ++i;
        }
        ++i;
        j = i + 1;
    }
    if (i*i > x) {
        --i;
    }
    return i;
}
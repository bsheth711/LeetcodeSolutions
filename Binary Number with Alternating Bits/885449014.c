bool hasAlternatingBits(int n){
    int prev = 3;
    int digit;

    while (n > 0) {
        digit = n % 2;

        if (digit == prev) {
            return false;
        }

        n /= 2;
        prev = digit;
    }

    return true;
}
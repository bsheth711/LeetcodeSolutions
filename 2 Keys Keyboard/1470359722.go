// prime factorization method
func minSteps(n int) int {
    if n == 1 {
        return 0
    }

    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            numTimes := n / i

            return minSteps(numTimes) + i
        }
    }

    return n
}
import (
    "math"
    "fmt"
)

// prime factorization method
func minSteps(n int) int {
    if n == 1 {
        return 0
    }

    sqrt := int(math.Sqrt(float64(n)))
    fmt.Println(sqrt)

    for i := 2; i <= sqrt ; i++ {
        if n % i == 0 {
            numTimes := n / i

            return minSteps(numTimes) + i
        }
    }

    return n
}
import "slices"

func mincostTickets(days []int, costs []int) int {
    dp := make([]int, 365+1)

    curDayIndex := 0
    
    for i := 1; i < len(dp); i++ {
        if curDayIndex >= len(days) ||
            i != days[curDayIndex] {
            dp[i] = dp[i-1]
        } else {

            fmt.Print("Day: ")
            fmt.Println(days[curDayIndex])

            best := math.MaxInt64

            // 1 day 
            bestDay := slices.Min(dp[i-1:i])
            best = min(best, bestDay + costs[0])
            fmt.Println(best)

            // 7 day
            bestDay = slices.Min(dp[max(0, i-7):i])
            best = min(best, bestDay + costs[1])
            fmt.Println(best)

            // 30 day
            bestDay = slices.Min(dp[max(0, i-30):i])
            best = min(best, bestDay + costs[2])
            fmt.Println(best)

            dp[i] = best

            curDayIndex++
        }
    }

    fmt.Println(dp)

    return dp[len(dp) - 1]
}
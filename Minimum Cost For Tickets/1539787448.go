import "slices"

func mincostTickets(days []int, costs []int) int {
    lastDay := days[len(days) - 1]
    dp := make([]int, lastDay + 1)

    curDayIndex := 0
    
    for i := 1; i < len(dp); i++ {        
        if i == days[curDayIndex] {

            best := math.MaxInt64

            // 1 day 
            bestDay := dp[i-1]
            best = min(best, bestDay + costs[0])

            // 7 day
            bestDay = slices.Min(dp[max(0, i-7):i])
            best = min(best, bestDay + costs[1])

            // 30 day
            bestDay = slices.Min(dp[max(0, i-30):i])
            best = min(best, bestDay + costs[2])

            dp[i] = best

            curDayIndex++
        } else {
            dp[i] = dp[i-1]
        }
    }

    return dp[len(dp) - 1]
}
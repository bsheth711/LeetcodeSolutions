import ("slices" 
        "math")

func minProcessingTime(processorTime []int, tasks []int) int {

    sort.Slice(tasks, func(i, j int) bool {
        return tasks[i] < tasks[j]
    })

    sort.Slice(processorTime, func(i, j int) bool {
        return processorTime[i] > processorTime[j]
    })
    
    longest := math.MinInt32

    for i, t := range processorTime { 
        longestTask := slices.Max(tasks[i*4:(i+1)*4])
        longest = max(longest, longestTask + t)
    }


    return longest
}
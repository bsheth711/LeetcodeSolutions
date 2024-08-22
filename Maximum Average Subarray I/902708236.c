double findMaxAverage(int* nums, int numsSize, int k){
    int curTotal = 0;
    double maxAvg = INT_MIN;

    for (int i = 0; i < numsSize; ++i) {
        curTotal += nums[i];

        if (i >= k - 1) {
            double avg = (double) curTotal / (double) k;

            if (avg > maxAvg) {
                maxAvg = avg;
            }

            curTotal -= nums[i - k + 1];
        }

    }

    return maxAvg;
}
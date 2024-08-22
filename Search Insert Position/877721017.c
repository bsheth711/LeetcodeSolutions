int searchInsert(int* nums, int numsSize, int target){
    int jump = (numsSize-1) / 2;
    int idx = (numsSize-1) / 2;

    if (nums[0] > target) {
        return 0; 
    }

    while (true) {
        if (idx < 0) {
            idx = 0;
        }
        if (idx >= numsSize) {
            idx = numsSize - 1;
        }

        jump /= 2;
        if (jump == 0) {
            ++jump;
        }

        if (nums[idx] == target) {
            return idx;
        }

        if (nums[idx] < target) { 
            if (idx == numsSize - 1) {
                return idx + 1;
            }
            else {
                if (nums[idx+1] > target) {
                    return idx + 1;
                }
            }
            idx += jump;
        }
        else {
            idx -= jump;
        }
    }
}
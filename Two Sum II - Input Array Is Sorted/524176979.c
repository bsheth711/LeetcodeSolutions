/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int* ret = malloc(sizeof(int) * 2);
    
    int i = 0;
    int j = numbersSize - 1;
    
    while (i < j) {
        int sum = numbers[i] + numbers[j];
        if (sum == target) {
            ret[0] = i + 1;
            ret[1] = j + 1;
            break;
        }
        else if (sum < target) {
            ++i;
        }
        else if (sum > target) {
            --j;
        }
    }
    
    *returnSize = 2;
    return ret;
}
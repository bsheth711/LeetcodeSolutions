/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int* sum = malloc(sizeof(int) * 2);
    
    int i = 0;
    int j = numbersSize - 1;
    
    while (i < j) {
        int temp = numbers[i] + numbers[j];
        if (temp == target) {
            sum[0] = i + 1;
            sum[1] = j + 1;
            break;
        }
        else if (temp < target) {
            ++i;
        }
        else if (temp > target) {
            --j;
        }
    }
    
    *returnSize = 2;
    return sum;
}
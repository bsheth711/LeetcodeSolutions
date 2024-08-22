class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1 
        smallest = sys.maxsize
 
        while start <= end: 
            mid = (start + end) // 2

            smallest = min(smallest, nums[mid])

            if nums[mid] < nums[end]:
                end = mid - 1 
            else:
                start = mid + 1
            '''
            if nums[start] > nums[end]:
                # search right
                start = mid + 1
            else:
                # search left
                end = mid - 1
            '''

        return smallest

        # 0, 1, 2, 3, 4
        # 2, 3, 4, 5, 0
        # 5, 1, 2, 3, 4
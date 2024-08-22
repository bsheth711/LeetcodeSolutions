class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = 0
        r = len(arr) - 1
        mid = (r + l) // 2

        while l <= r:
            #print(arr[l:r])
            mid = (r + l) // 2
            if arr[mid] == x:
                break
            elif arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        
        curDiff = abs(arr[mid] - x)
        while mid - 1 >= 0 and abs(arr[mid - 1] - x) <= curDiff:
            mid -= 1
            curDiff = abs(arr[mid] - x)
        
        ret = []
        l = mid
        r = mid + 1

        while len(ret) < k:
            leftChoice = sys.maxsize
            if l >= 0:
                leftChoice = abs(arr[l] - x)

            rightChoice = sys.maxsize
            if r < len(arr):
                rightChoice = abs(arr[r] - x)

            if leftChoice <= rightChoice:
                ret.append(arr[l])
                l -= 1
            else:
                ret.append(arr[r])
                r += 1

        ret.sort()
        '''
        if l < 0:
            l = 0
        if r > len(arr):
            r = len(arr)
        '''

        return ret




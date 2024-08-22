class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        count = 0

        while j < n:
            if i >= m + count:
                nums1[i] = nums2[j]
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1
                
            else:
                for k in range(len(nums1) - 1, i, -1):
                    nums1[k] = nums1[k-1]
                
                nums1[i] = nums2[j]
                count += 1
                i += 1
                j += 1
  

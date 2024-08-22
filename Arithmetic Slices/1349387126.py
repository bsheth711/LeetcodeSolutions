class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        differences = []

        for i in range(len(nums) - 1):
            differences.append(nums[i] - nums[i + 1])
        
        print(differences)

        cur = None
        counter = 0
        total = 0
        for difference in differences:
            if cur == difference:
                counter += 1
            else:
                cur = difference
                counter = 0

            print(counter)
            if counter > 0:
                total += counter

        return total
    

        


'''
0=>0
1=>0
2=>1
3=>3
4=>6
5=>10
6=>15
7=>21
8=>28
9=>36

'''
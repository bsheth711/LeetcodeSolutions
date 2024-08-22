class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        ls = []
        ls.extend(self.generate(numRows-1))

        new = []
        last = 0
        for num in ls[numRows-2]:
            new.append(num+last)
            last = num

        new.append(1) 
        ls.append(new)
        return ls
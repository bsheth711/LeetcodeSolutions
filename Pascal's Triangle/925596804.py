class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        ls = []

        def recurse(numRows):
            nonlocal ls
            if numRows == 1:
                ls.append([1])
                return
    
            recurse(numRows-1)
    
            print(f"numRows: {numRows}, ls: {ls}")
    
            new = [] 
            last = 0
            for num in ls[numRows-2]:
                new.append(num+last)
                last = num
            
            new.append(1)
    
            ls.append(new)
        
        recurse(numRows)

        return ls
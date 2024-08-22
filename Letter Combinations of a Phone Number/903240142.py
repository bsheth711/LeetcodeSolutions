class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        ls = [""]

        for char in digits:
            match char:
                case "2":
                    ls = self.apply(ls, "abc")
                case "3":
                    ls = self.apply(ls, "def")
                case "4":
                    ls = self.apply(ls, "ghi")
                case "5":
                    ls = self.apply(ls, "jkl")
                case "6":
                    ls = self.apply(ls, "mno")
                case "7":
                    ls = self.apply(ls, "pqrs")
                case "8":
                    ls = self.apply(ls, "tuv")
                case "9":
                    ls = self.apply(ls, "wxyz")
        
        return ls
    
    def apply(self, ls, letters):
        toAppend = []

        for combo in ls:
            for letter in letters:
                toAppend.append("" + combo + letter)

        return toAppend

                
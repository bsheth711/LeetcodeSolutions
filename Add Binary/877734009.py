class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""

        longest =  len(a)
        if len(b) > len(a):
            longest = len(b)

        for i in range(longest):
            x = 0
            y = 0

            if len(a) - 1 - i >= 0:
                x = int(a[len(a) - 1 - i])

            if len(b) - 1 - i >= 0:
                y = int(b[len(b) - 1 - i])

            match x + y + carry:
                case 0:
                    ans = "0" + ans
                    carry = 0
                case 1:
                    ans = "1" + ans
                    carry = 0
                case 2:
                    ans = "0" + ans
                    carry = 1
                case 3:
                    ans = "1" + ans
                    carry = 1

        if carry != 0:
            ans = "1" + ans

        return ans
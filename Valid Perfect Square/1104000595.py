class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # 1, 2, 3, 4, 5, 6, 7, 8, 9
        # 1, 4, 9, 16, 25, 36, 49, 64, 81

        l = 0
        r = num

        while l < r:
            mid = (l + r) // 2
            sq = mid ** 2
            print(mid)
            print(sq)

            if sq == num:
                break
            elif sq < num:
                l = mid + 1
            else:
                r = mid - 1

        mid = (l + r) // 2
        sq = mid ** 2 

        print(mid)
        print(sq)

        return sq == num
class Solution:
    def fib(self, n: int) -> int:
        counter = 1

        arr = []
        arr.append(0)
        arr.append(1)

        if n == 0:
            return arr[0]
        if n == 1:
            return arr[1]

        while counter < n:
            tmp = arr[0] + arr[1]
            arr[0] = arr[1]
            arr[1] = tmp
            counter += 1

        return arr[1]
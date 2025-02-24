class Solution:
    def fib(self, n: int) -> int:
        result = [0] * (n+1) # n+1 as n in inclusive
        if n <= 1:
                return n
        result[0] = 0
        result[1] = 1
        for i in range(2, n+1): # n+1 as n in inclusive
            result[i] = result[i-1] + result[i-2]
        return result[n]
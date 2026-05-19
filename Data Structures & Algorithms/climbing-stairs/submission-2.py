class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        prev = 2
        prevprev = 1

        k = 3
        distinctSteps = 3

        while True:
            if k == n:
                return distinctSteps
            k += 1
            temp = prev
            prev = distinctSteps
            prevprev = temp
            distinctSteps = prev + prevprev


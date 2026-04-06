from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        #Base case
        #1 -> 1 step -> 1 way
        #2 -> 2 steps, 1 + 1, 2 -> 2 ways
        #3 -> 3 steps, 1 + 1 + 1, 1 + 2 , 2 + 1 , 3 ways
        if n == 1:
            return 1

        if n == 2:
            return 2


        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
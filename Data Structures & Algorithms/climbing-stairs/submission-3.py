class Solution:
    #Bottom up approach
    #Start from smallest problem and work our way up
    def climbStairs(self, n: int) -> int:
        # 1 -> 1 step 
        # 2 -> 2 step
        # Keep memoize cache so we don't have to recompute solution
        memo = [0]*(n+1)
        memo[1],memo[2] = 1,2

        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
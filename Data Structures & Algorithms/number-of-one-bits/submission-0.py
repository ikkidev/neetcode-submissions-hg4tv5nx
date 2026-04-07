class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n > 0:
            if n & 1 == 1:
                count+=1
        
            # Shift bit to the right
            # Equivalent to n = n >> 2
            n = n // 2
            
        return count

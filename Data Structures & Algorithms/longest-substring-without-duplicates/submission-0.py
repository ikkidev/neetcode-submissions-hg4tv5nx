class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Intuition keep a window of longest string encountered so far
        #O(n) Time worst
        #O(m) Space -> m : number of unique chars
        L = 0
        longest = 1
        window = set()
        window.add(s[L])

        for R in range(1,len(s)):

            while s[R] in window:
                window.remove(s[L])
                L+=1
            window.add(s[R])
            curLength=R-L+1
            longest = max(longest, curLength)

        return longest
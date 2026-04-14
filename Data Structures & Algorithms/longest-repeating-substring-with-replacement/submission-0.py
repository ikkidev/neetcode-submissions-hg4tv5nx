class Solution:

    # Fail, had to get hint to solve. Key insight is to use a dict map to keep
    # track off the frequency of the most common char in a window
    # Set is not sufficient here
    # def characterReplacement(self, s: str, k: int) -> int:
    #     # Sliding window
    #     L = 0
    #     #min s length is 1
    #     longest = 1
    #     #keep track of replacement done
    #     replace = 0
    #     window = set()
    #     window.add(s[L])


    #     # Goal, do k replacement of string that gives us the longest window where all char in s is the same char
    #     for R in range(1,len(s)):

    #         while s[R] not in window and replace < k:
    #             replace += 1
    #             L+=1     

    #         curLength = R-L+1
    #         longest = max(curLength, longest)


    #     return longest
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Track frequency of each character in current window
        L = 0
        max_freq = 0
        longest = 0
        
        for R in range(len(s)):
            # Add current character to window
            count[s[R]] = count.get(s[R], 0) + 1
            max_freq = max(max_freq, count[s[R]])
            
            # Check if current window is valid
            # (window_length - max_freq) = number of replacements needed
            while (R - L + 1) - max_freq > k:
                # Window is invalid, shrink from left
                count[s[L]] -= 1
                L += 1
            
            # Update longest valid window
            longest = max(longest, R - L + 1)
        
        return longest
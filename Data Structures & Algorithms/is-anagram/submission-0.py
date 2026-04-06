class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s_copy  = ''.join(sorted(s.lower()))
        t_copy = ''.join(sorted(t.lower()))

        index = 0
        while index < len(s):
            if s_copy[index] != t_copy[index]:
                return False
            else: 
                index += 1

        return True



        
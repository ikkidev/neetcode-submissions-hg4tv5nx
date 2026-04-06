class Solution:
    def scoreOfString(self, s: str) -> int:

        prev = 0
        sum = 0
        for i in range(1, len(s)):
            prev = i - 1
            prev_c = s[prev].lower()
            current_c = s[i].lower()

            print(prev_c)
            print(current_c)
            sum += abs(int(ord(current_c)) - int(ord(prev_c)))

        return sum

        
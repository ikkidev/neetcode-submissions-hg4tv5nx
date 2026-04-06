class Solution:

    #Intuition: Need a way to figure out when a word starts and ends
    #Prefix word with the length of the word and use a delimiter
    #So we can distinguish when a number is the length of the word vs
    #when it's actually part of a word 
    def encode(self, strs: List[str]) -> str:
        delimiter = '|'
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + delimiter + word

        return encoded



    def decode(self, s: str) -> List[str]:
        delimiter = '|'
        
        length = ""
        words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != delimiter:
                j += 1
            length = int(s[i:j])
            words.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return words

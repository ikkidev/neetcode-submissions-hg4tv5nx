class Solution:

    #1st intuition
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Strategy construct a map of char frequency for each string
        #Check if any char map is equal
        #If they are, add them into a grouping

        anagram_map = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for character in s:
                char_index = ord(character) - ord('a')
                count[char_index] += 1
            #hashmap keys have to be immutable in python
            anagram_map[tuple(count)].append(s)
        print (anagram_map)
        return list(anagram_map.values())

    #2nd intuition
    #Sort 



        
class TrieNode:
    def __init__(self):
        #Dict to keep track of children
        #children is a dict of TrieNode
        self.children = {}
        #Var to keep track of end of word
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            #Insert char if it's not already in the trie
            if c not in cur.children:
                cur.children[c] = TrieNode()
            #Otherwise iterate keep following char prefix in the tree
            cur = cur.children[c]
        # Reached the end of word, mark last char as end of word
        cur.is_word = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            #If char is not in prefix, we know the full word cannot be in the tre
            if c not in cur.children:
                return False
            #Otherwise iterate keep following char prefix in the tree
            cur = cur.children[c]

        # Do we need to check for cur.word is True ?
        # My intuition says no because the word can be part of a longer word in the trie

        # Nevermind we do need to check that it's a word
        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            #If char is not in prefix, we know the full word cannot be in the tre
            if c not in cur.children:
                return False
            #Otherwise iterate keep following char prefix in the tree
            cur = cur.children[c]

        # Don't need to check is_word here
        # we consider the prefix to be in the tree even if it happens to be a word
        return True
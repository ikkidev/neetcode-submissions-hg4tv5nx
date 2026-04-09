class TrieNode:
    def __init__(self):
        # Dictionary: char -> TrieNode
        self.children = {}
        self.is_word = False

class WordDictionary:
# Can use Trie to ensure search time complexity is efficient O(k) where K is the string length to be searched
# Dicts are only efficient for full word search

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Add word into Trie
        cur = self.root

        # Search for char in word
        # Need to handle '.'
        # where dot can match with any children
        # So dfs ?
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def dfs(self, index, word, node) -> bool:
        #TODO implement dfs for searching word on '.'
        # base_case 
        if index == len(word):
            return node.is_word

        # Do we need to keep track of visited nodes?
        # visited = set()
        # No we don't because we only ever move forward through the trie nodes
        # and there is no possibility of running into a cycle

        #Get char being searched 
        c = word[index]
        if "." == c:
            for child in node.children.values():
                if self.dfs(index+1, word, child):
                    return True
            return False
        else:
            if c not in node.children:
                return False

        return self.dfs(index+1, word, node.children[c])

    def search(self, word: str) -> bool:
        cur = self.root
        return self.dfs(0, word, self.root)
        

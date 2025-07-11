class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        if not self.search(word):
            i = 0
            curr_trie = self.trie
            for c in word:
                if c not in curr_trie.children:
                    curr_trie.children[c] = TrieNode()
                curr_trie = curr_trie.children[c]
            curr_trie.endOfWord = True



        

    def search(self, word: str) -> bool:
        i = 0
        curr_trie = self.trie
        while i < len(word):
            char = word[i]
            if char not in curr_trie.children:
                return False                
            curr_trie = curr_trie.children[char]
            i += 1
        if not curr_trie.endOfWord:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        i = 0
        curr_trie = self.trie
        while i < len(prefix):
            char = prefix[i]
            if char not in curr_trie.children:
                return False
            curr_trie = curr_trie.children[char]
            i += 1
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
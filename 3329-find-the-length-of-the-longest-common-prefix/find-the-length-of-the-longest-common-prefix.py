class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
    

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie1 = Trie()
        trie2 = Trie()
        for num in arr1:
            trie1.insert(str(num))
        for num in arr2:
            trie2.insert(str(num))
        lcp = 0
        
        for num in arr2:
            curr_lcp = 0
            curr = trie1.root
            for char in str(num):
                if char in curr.children:
                    curr = curr.children[char]
                    curr_lcp += 1
                    lcp = max(curr_lcp, lcp)
                else:
                    break
        
        
        return lcp

                

        
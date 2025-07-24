class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.endOfWord = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        trie = TrieNode()

        # Build the Trie
        for word in strs:
            if not word:
                return ""  # If any word is empty, no common prefix
            curr = trie
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                curr.count += 1
            curr.endOfWord = True

        # Traverse the Trie to find common prefix
        res = ""
        curr = trie
        while len(curr.children) == 1:
            for char in curr.children:
                next_node = curr.children[char]
                if next_node.count < len(strs):
                    return res
                res += char
                curr = next_node
                break
            # char, next_node = next(iter(curr.children.items()))
           
          

        return res

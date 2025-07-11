class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str)-> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
    
    def search(self, word: str)-> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord
    
    def startsWith(self, prefix:str)-> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = TrieNode()
        extra_chars = float('inf')

        def insert(word: str, node: TrieNode)-> None:
            curr = node
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True
        
        for word in dictionary:
            insert(word, trie)
        
        # # Simple DFS
        # dict_set = set(dictionary)
        # dp = {}
        # def dfs(i):
        #     if i == len(s):
        #         return 0
            
        #     if i in dp:
        #         return dp[i]
            
        #     # skip
        #     res = 1 + dfs(i+1)

        #     for j in range(i, len(s)):
        #         if s[i:j+1] in dict_set:
        #             res = min(res, dfs(j+1))

        #     dp[i] = res
        #     return res
        
        # return dfs(0)
        
        #  DFS Using trie
        dp = {}
        def dfs(i):
            if i == len(s):
                return 0
            
            if i in dp:
                return dp[i]
            # skip
            res = 1 + dfs(i+1)

            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.endOfWord:
                    res = min(res, dfs(j+1))

            dp[i] = res
            return res
        
        return dfs(0)

            

        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
    
    def insertAll(self, words):
        for word in words:
            self.insert(word)
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord
    
    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(board), len(board[0])

        # # No Trie solution - Passes 64/65 cases - TLE for case 65
        # words_set = set(words)
        # max_len = max(len(word) for word in words)
        # visited = set()
        # res = []

        # def dfs(r, c, path):
        #     if len(path) > max_len:
        #         return 
        #     word = ''.join(path)
        #     if word in words_set:
        #         res.append(word)
        #         words_set.remove(word)
            
        #     for dr, dc in directions:
        #             row, col = r+dr, c+dc
        #             if 0<= row < rows and 0 <= col < cols and (row, col) not in visited:
        #                 visited.add((row, col))
        #                 path.append(board[row][col])
        #                 dfs(row, col, path)
        #                 path.pop()
        #                 visited.remove((row, col))
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if words_set:
        #             visited.add((r, c))
        #             dfs(r, c, [board[r][c]])
        #             visited.remove((r, c))
        # return res


        # # Trie solution  -  Solved without any external help
        # trie = Trie()
        # trie.insertAll(words)
        # max_len = max(len(word) for word in words)
        # visited = set()
        # res = set()

        # def dfs(r, c, path, node):
        #     if len(path) > max_len:
        #         return 
        #     if node.endOfWord:
        #         word = ''.join(path)
        #         res.add(word)
                
        #     for dr, dc in directions:
        #             row, col = r+dr, c+dc
        #             if 0<= row < rows and 0 <= col < cols and (row, col) not in visited:
        #                 curr_char = board[row][col]
        #                 if curr_char not in node.children:
        #                     continue
        #                 path.append(curr_char)
        #                 visited.add((row, col))
        #                 dfs(row, col, path, node.children[curr_char])
        #                 path.pop()
        #                 visited.remove((row, col))
        
        # for r in range(rows):
        #     for c in range(cols):
        #         node = trie.root
        #         char = board[r][c]
        #         if char in node.children:
        #             visited.add((r, c))
        #             dfs(r, c, [board[r][c]], node.children[char])
        #             visited.remove((r, c))
        # return list(res)

        # Trie solution  - Optimizations
        trie = Trie()
        trie.insertAll(words)
        visited = set()
        # res = set()
        res = []

        def dfs(r, c, path, node):
            if node.endOfWord:
                word = ''.join(path)
                res.append(word)
                node.endOfWord = False
                
            for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if 0<= row < rows and 0 <= col < cols and (row, col) not in visited:
                        curr_char = board[row][col]
                        if curr_char not in node.children:
                            continue
                        path.append(curr_char)
                        visited.add((row, col))
                        dfs(row, col, path, node.children[curr_char])
                        path.pop()
                        visited.remove((row, col))
        
        for r in range(rows):
            for c in range(cols):
                node = trie.root
                char = board[r][c]
                if char in node.children:
                    visited.add((r, c))
                    dfs(r, c, [board[r][c]], node.children[char])
                    visited.remove((r, c))
        return res

       

        
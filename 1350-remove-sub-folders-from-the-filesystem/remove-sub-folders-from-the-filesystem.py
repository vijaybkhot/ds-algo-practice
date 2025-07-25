class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
    
    def insertIfNoPrefix(self, parts):
        curr = self.root
        for part in parts:
            if curr.endOfWord:
                return False
            if part not in curr.children:
                curr.children[part] = TrieNode()
            
            curr = curr.children[part]
        curr.endOfWord = True
        return True
    
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord
    
    def isPrefix(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True



class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        res = []
        folder.sort()

        # for subfolder in folder:
        #     i = len(subfolder)-1
        #     while i >= 0:
        #         while i >= 0 and subfolder[i] != '/':
        #             i -= 1
        #         parent_folder = subfolder[:i]
        #         if trie.search(parent_folder):
        #             break
        #         i -= 1
        #     if i < 0:    
        #         trie.insert(subfolder)
        #         res.append(subfolder)
            
        # return res

        # Using a set to store parent and check each parent of the folder if it already exists
        parent_set = set()
        for subfolder in folder:
            i = len(subfolder)-1
            while i >= 0:
                while i >= 0 and subfolder[i] != '/':
                    i -= 1
                parent_folder = subfolder[:i]
                # if trie.search(parent_folder):
                if parent_folder in parent_set:
                    break
                i -= 1
            if i < 0:    
                trie.insert(subfolder)
                res.append(subfolder)
                parent_set.add(subfolder)
            
        return res

        # # Optimized approach - Insert in trie only if no prefix is found
        # for subfolder in folder:
        #     parts = subfolder.split('/')[1:]
        #     if trie.insertIfNoPrefix(parts):
        #         res.append(subfolder)
        
        # return res

        

        # Sorting and startswith
        res.append(folder[0])
        for subfolder in folder[1:]:
            parent = res[-1]+'/'
            if subfolder.startswith(parent):
                continue
            res.append(subfolder)
        return res

            
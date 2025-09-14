class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()
    
    def insert(self, word):
        curr = self.trie
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
    
    def search(self, word):
        res = []
        curr = self.trie
        for char in word:
            if char in curr.children:
                res.append(char)
                curr = curr.children[char]
            elif char.lower() in curr.children:
                res.append(char.lower())
                curr = curr.children[char.lower()]
            else:
                return ""
        if curr.endOfWord:
            return ''.join(res)
        else:
            return ""
    



class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # lower_cap_list= { word.lower():idx for idx, word in enumerate(wordlist)}

        # trie = Trie()
        # for word in wordlist:
        #     trie.insert(word)
        
        # res = [trie.search(word) for word in queries]
        # return res
        def devowel(word: str) -> str:
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())

        word_set = set(wordlist)


        lower_cap_map = {}
        devowel_map = {}

        for idx, word in enumerate(wordlist):
            if word.lower() not in lower_cap_map:
                lower_cap_map[word.lower()] = idx
            key = devowel(word)
            if key not in  devowel_map:
                devowel_map[key] = idx
        
        res = []
        for word in queries:
            if word in word_set:
                res.append(word)
                continue
            elif word.lower() in lower_cap_map:
                res.append(wordlist[lower_cap_map[word.lower()]])
            elif devowel(word) in devowel_map:
                res.append(wordlist[devowel_map[devowel(word)]])
                # found = False
                # for target in lower_cap_map:
                #     if len(target) != len(word):
                #         continue
                #     matching = True

                #     for i in range(len(word)):
                #         if word[i] == target[i] or word[i].lower() == target[i]:
                #             continue
                #         elif word[i] in "aeiouAEIOU" and target[i] in "aeiou":
                #             continue
                #         else:
                #             matching = False
                #             break
                #     if matching:
                #         res.append(wordlist[lower_cap_map[target]])
                #         found = True
                #         break
                # if not found:
                #     res.append("")
            else:
                res.append("")
           
        
        return res


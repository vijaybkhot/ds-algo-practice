class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        q = deque([(beginWord, 1)])
        num_words = 0
        visited = set()

        def get_neighbors(word, wordListSet):
            neighbors = set()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != word[i]:
                        new_word = list(word)      
                        new_word[i] = c            
                        new_word = ''.join(new_word)  
                        if new_word in wordListSet:
                            neighbors.add(new_word)
            return neighbors    


        while q:
            word, num_words = q.popleft()
            if word == endWord:
                return num_words
            visited.add(word)
            
            adj_words = get_neighbors(word, words)
            for new_word in adj_words:
                if new_word not in visited:
                    q.append((new_word, num_words+1))
        
        return 0
            
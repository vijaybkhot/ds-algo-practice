class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        q = deque([(beginWord, 1)])
        num_words = 0
        visited = set()

        def get_adjacent_words(word):
            word_list = [char for char in word]
            adj_words = []
            for idx, char in enumerate(word_list):
                for new_char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word_list[::]
                    new_word[idx] = new_char
                    new_word = ''.join(new_word)
                    if new_word in words:
                        adj_words.append(new_word)
            
            return adj_words


        while q:
            word, num_words = q.popleft()
            if word == endWord:
                return num_words
            visited.add(word)
            
            adj_words = get_adjacent_words(word)
            for new_word in adj_words:
                if new_word not in visited:
                    q.append((new_word, num_words+1))
        
        return 0
            
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        char_sets = [set()] * len(beginWord)
        # Accumulate unique index wise character for all words in wordList
        for word in wordList:
            for idx, char in enumerate(word):
                char_sets[idx].add(char)
        
        wordSet = set(wordList)

        visited = set()
        def getAdjacentWords(word):
            adj = []
            for i in range(len(beginWord)):
                for char in char_sets[i]:
                    curr_word = word[:i] + char + word[i+1:]
                    if curr_word not in visited and curr_word in wordSet:
                        visited.add(curr_word)
                        adj.append(curr_word)
            return adj

        q = deque()
        q.append((beginWord, 0))
        dist = 0
        while q:
            curr_word, curr_dist = q.popleft()
            if curr_word == endWord:
                return curr_dist+1
            for nei in getAdjacentWords(curr_word):
                q.append((nei, curr_dist+1))
        
        return 0


        
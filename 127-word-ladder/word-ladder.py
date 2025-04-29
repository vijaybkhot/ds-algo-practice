class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # char_sets = [set()] * len(beginWord)
        # Accumulate unique index wise character for all words in wordList
        # for word in wordList:
        #     for idx, char in enumerate(word):
        #         char_sets[idx].add(char)
        
        wordSet = set(wordList)
        wordSet.add(beginWord)
        visited = set()

        def getAdjacentWords(word):
            adj = []
            for i in range(len(beginWord)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char != word[i]:
                        curr_word = word[:i] + char + word[i+1:]
                        if curr_word in wordSet:
                            adj.append(curr_word)
            return adj
        # One directional BFS
        q = deque()
        q.append((beginWord, 0))
        dist = 0
        while q:
            curr_word, curr_dist = q.popleft()
            if curr_word == endWord:
                return curr_dist+1
            for nei in getAdjacentWords(curr_word):
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, curr_dist+1))
        
        return 0

        # # Bi-directional BFS
        # begin = {beginWord}
        # end = {endWord}
        # dist = 1

        
        # while begin and end:
        #     if len(begin) > len(end):
        #         begin, end = end, begin

        #     temp = set()
        #     for word in begin:
        #         visited.add(word)
        #         for nei in getAdjacentWords(word):
        #             if nei in end:
        #                 return dist + 1
        #             if nei not in visited:
        #                 visited.add(nei)
        #                 temp.add(nei)

        #     begin = temp
        #     dist += 1
                        
        
        # return 0


        
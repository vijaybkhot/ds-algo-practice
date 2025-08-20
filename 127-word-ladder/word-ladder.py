class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        def get_neighbors(word, words):
            adjacents = set()
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char != word[i]:
                        # build the new word by slicing instead of copying lists
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in words:
                            adjacents.add(new_word)
            return adjacents


        q = deque([(beginWord, 1)])
        num_words = 0
        visited = set()

        left, right = deque(), deque()
        left.append(beginWord)
        right.append(endWord)
        left_visited_set = {beginWord}
        right_visited_set = {endWord}
        level = 1

        while left and right:
            if len(left) > len(right):
                left, right = right, left
                left_visited_set, right_visited_set = right_visited_set, left_visited_set
            
            
            for _ in range(len(left)):
                curr_word = left.popleft()
                adjacents = get_neighbors(curr_word, words)
                for nei in adjacents:
                    if nei in right_visited_set:
                        return level + 1
                    if nei not in left_visited_set:
                        left_visited_set.add(nei)
                        left.append(nei)
            level += 1
        
        return 0
        
            
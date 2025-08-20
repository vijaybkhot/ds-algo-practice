class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

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
        
            
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        char_dict = {char: index for index, char in enumerate(order)}

        if len(words) == 1:
            return True
        i, j = 0, 1

        while j < len(words):
            isSorted = False
            word1 = words[i]
            word2 = words[j]
            l, r = 0, 0
            while l < len(word1) and r < len(word2):
                if word1[l] == word2[r]:
                    l += 1
                    r += 1
                elif char_dict[word1[l]] < char_dict[word2[r]]:
                    isSorted = True
                    break
                elif char_dict[word1[l]] > char_dict[word2[r]]:
                    break
            if l < len(word1) and r >= len(word2):
                isSorted = False
            
            if l >= len(word1) and r < len(word2):
                isSorted = True
            
            if l >= len(word1) and r >= len(word2):
                isSorted = True

            if not isSorted:
                return False
            
            i += 1
            j += 1
        
        return True


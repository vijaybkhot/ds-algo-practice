class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0

        words = text.split(' ')
        for word in words:
            add = True
            for char in brokenLetters:
                if char in word:
                    add = False
                    break
            if add:
                count += 1
        
        return count
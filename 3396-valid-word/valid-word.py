class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        isVowel, isConsonant = False, False
        for c in word:
            if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                return False

            if c in 'AEIOUaeiou':
                isVowel = True
            elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" and c not in 'AEIOUaeiou':
                isConsonant = True
        
        return isVowel and isConsonant
         

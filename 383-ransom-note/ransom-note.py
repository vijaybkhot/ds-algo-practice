class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)

        for char in note_counter:
            if note_counter[char] > mag_counter[char]:
                return False
        
        return True
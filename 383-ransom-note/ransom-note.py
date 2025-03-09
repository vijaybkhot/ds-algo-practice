class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Create ransomNote map:
        r_note_map = {}
        magazine_map = {}
        for char in ransomNote:
            r_note_map[char] = r_note_map.get(char, 0) + 1
        for char in magazine:
            magazine_map[char] = magazine_map.get(char, 0) + 1
        
        
        for key in r_note_map.keys():
            if key not in magazine_map or r_note_map[key] > magazine_map[key]:
                return False
        
        return True

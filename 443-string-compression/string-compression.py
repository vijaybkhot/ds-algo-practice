class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        i = 0
        while i < len(chars):
            curr_char = chars[i]
            i += 1
            repeat = 1
            while i < len(chars) and chars[i] == curr_char:
                repeat += 1
                i += 1
            chars[insert] = curr_char
            insert += 1
            if repeat > 1:
                repeat = str(repeat)
                for char in repeat:
                    chars[insert] = char
                    insert += 1
        
        return insert

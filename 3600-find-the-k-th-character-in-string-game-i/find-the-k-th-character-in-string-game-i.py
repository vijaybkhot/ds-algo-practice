class Solution:
    def kthCharacter(self, k: int) -> str:

        res = "a"
        while len(res) < k:
            curr_res = res
            for char in curr_res:
                next_char = chr(ord(char)+1) if char != 'z' else 'a'
                res += next_char
        
        return res[k-1]

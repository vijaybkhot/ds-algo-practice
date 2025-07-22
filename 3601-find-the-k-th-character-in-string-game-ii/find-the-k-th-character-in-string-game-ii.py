class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        # # Brute Force appraoch - TLE
        # res = 'a'
        # next_char_map = {
        #     'a':'b',
        #     'b': 'c',
        #     'c': 'd',
        #     'd': 'e',
        #     'e': 'f',
        #     'f':'g',
        #     'g': 'h',
        #     'h': 'i',
        #     'i': 'j',
        #     'j':'k',
        #     'k': 'l',
        #     'l': 'm',
        #     'm': 'n',
        #     'n':'o',
        #     'o': 'p',
        #     'p': 'q',
        #     'q': 'r',
        #     'r':'s',
        #     's': 't',
        #     't': 'u',
        #     'u': 'v',
        #     'v':'w',
        #     'w': 'x',
        #     'x': 'y',
        #     'y': 'z',
        #     'z': 'a',

        # }
        # for operation in operations:
        #     curr_str = res
        #     if operation == 0:
        #         res += curr_str
        #     else:
        #         for char in res:
        #             new_char = next_char_map[char]
        #             curr_str += new_char
                
        #         res = curr_str
        

        # return res[k-1]

        count_ops = 0
        val = k
        while val > 1:
            jumps = math.ceil(math.log2(val))
            val -= 2 ** (jumps - 1)
            count_ops += operations[jumps - 1]
        return chr(ord('a') + (count_ops % 26))
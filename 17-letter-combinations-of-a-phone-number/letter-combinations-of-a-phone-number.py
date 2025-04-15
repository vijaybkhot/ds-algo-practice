class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # # Attempt I
        # res = []
        # def backtrack(start, path):
        #     if start >= len(digits):
        #         if len(path)>0 and len(path) == len(digits):
        #             res.append(''.join(path[:]))
        #         return
            
        #     for i in range(start, len(digits)):
        #         curr_chars = num_to_char_map[digits[i]]
        #         for char in curr_chars:
        #             path.append(char)
        #             backtrack(i+1, path)
        #             path.pop()

        # Simplified code
        if not digits:
            return []

        res = []
        

        def backtrack(index, path):
            if index == len(digits):
                res.append(''.join(path[:]))
                return
            
            for char in num_to_char_map[digits[index]]:
                path.append(char)
                backtrack(index+1, path)
                path.pop()

        
        backtrack(0, [])
        return res

        
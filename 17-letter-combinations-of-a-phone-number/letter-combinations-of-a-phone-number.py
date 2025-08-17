class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_char_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        n = len(digits)
        res = []
        if len(digits) == 0:
            return []
        def dfs(i, curr_str):
            if i == n:
                res.append(curr_str)
                return
            
            digit = digits[i]
            if digit in digit_char_map:
                for char in digit_char_map[digit]:
                    dfs(i+1, curr_str+char)


        dfs(0, "")

        return res

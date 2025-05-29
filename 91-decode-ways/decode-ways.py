class Solution:
    def numDecodings(self, s: str) -> int:

        # # First attempt: Simple recursion
        # if s[0] == "0":
        #     return 0
        
        # number_to_char_map = {
        #     '1': [['A']],
        #     '2': [['B']],
        #     '3': [['C']],
        #     '4': [['D']],
        #     '5': [['E']],
        #     '6': [['F']],
        #     '7': [['G']],
        #     '8': [['H']],
        #     '9': [['I']],
        #     '10': [['J']],
        #     '11': [['A', 'A'], ['K']],
        #     '12': [['A', 'B'], ['L']],
        #     '13': [['A', 'C'],  ['M']],
        #     '14': [['A', 'D'], ['N']],
        #     '15': [['A', 'E'], ['O']],
        #     '16': [['A', 'F'], ['P']],
        #     '17': [['A', 'G'], ['Q']],
        #     '18': [['A', 'H'], ['R']],
        #     '19': [['A', 'I'], ['S']],
        #     '20': [['T']],
        #     '21': [['B', 'A'], ['U']],
        #     '22': [['B', 'B'], ['V']],
        #     '23': [['B', 'C'], ['W']],
        #     '24': [['B', 'D'], ['X']],
        #     '25': [['B', 'E'], ['Y']],
        #     '26': [['B', 'F'], ['Z']],

        # }

           
        
        # self.count = 0
        # def dfs(i):
        #     if i >= len(s):
        #         self.count += 1
        #         return
            
        #     for j in range(2):
        #         if i+j+1 > len(s) or s[i:i+j+1] not in number_to_char_map:
        #             break
        #         dfs(i+j+1)
        
        # dfs(0)

        # return self.count


        # More clean approach using memoization
        if not s or s[0] == "0":
            return 0
        
        @lru_cache(maxsize=None)
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            count = dfs(i + 1)  # Single digit
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                count += dfs(i + 2)  # Two digits
            return count
        
        return dfs(0)
            

        

        

        
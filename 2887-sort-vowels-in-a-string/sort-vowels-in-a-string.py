class Solution:
    def sortVowels(self, s: str) -> str:
        s_map = Counter(s)
        vowel_count = [[char, count] for char, count in s_map.items() if char in "aeiouAEIOU"]
        # vowel_count.sort(key=lambda x: x[0], reverse=True)
        # Using count sort:
        sorted_vowels = [['A', 0], ['E', 0], ['I', 0], ['O', 0], ['U', 0], ['a', 0], ['e', 0], ['i', 0], ['o', 0], ['u', 0]]
        for char, count in vowel_count:
            for i in range(len(sorted_vowels)):
                if sorted_vowels[i][0] == char:
                    sorted_vowels[i][1] = count
                    break
        


        res = [char for char in s]
        vowel_pointer = 0
        for i in range(len(res)):
            if res[i] in "AEIOUaeiou":
                while sorted_vowels[vowel_pointer][1] == 0:
                    vowel_pointer += 1
                res[i] = sorted_vowels[vowel_pointer][0]
                sorted_vowels[vowel_pointer][1] -= 1
                # vowel_count[-1][1] -= 1
                # if vowel_count[-1][1] == 0:
                #     vowel_count.pop()

        return ''.join(res)




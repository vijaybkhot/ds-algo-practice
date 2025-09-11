class Solution:
    def sortVowels(self, s: str) -> str:
        s_map = Counter(s)
        vowel_count = [[char, count] for char, count in s_map.items() if char in "aeiouAEIOU"]
        vowel_count.sort(key=lambda x: x[0], reverse=True)

        res = [char for char in s]
        for i in range(len(res)):
            if res[i] in "AEIOUaeiou":
                res[i] = vowel_count[-1][0]
                vowel_count[-1][1] -= 1
                if vowel_count[-1][1] == 0:
                    vowel_count.pop()

        return ''.join(res)




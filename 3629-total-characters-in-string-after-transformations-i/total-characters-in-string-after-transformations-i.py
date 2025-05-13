class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        # # First attempt:
        # chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # char_count = [0] * 26
        # for char in s:
        #     char_idx = chars.index(char)
        #     char_count[char_idx] += 1
        # for _ in range(t):
        #     temp = char_count[:]
        #     for i in range(26):
        #         if i > 0 and i < 26:
        #             char_count[i] = temp[i-1]
        #         if i == 25:
        #             char_count[0] = temp[i]
        #             char_count[1] += temp[i]
        
        # MOD = 10**9 + 7
        # return sum(char_count) % MOD

        # Optimized approach:
        MOD = 10**9 + 7
        char_count = [0] * 26
        
        for char in s:
            char_count[ord(char) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            for i in range(25):  # 'a' to 'y'
                new_count[i + 1] = char_count[i]
            # 'z' becomes 'a' and 'b'
            new_count[0] += char_count[25]
            new_count[1] += char_count[25]
            char_count = new_count

        return sum(char_count) % MOD

        
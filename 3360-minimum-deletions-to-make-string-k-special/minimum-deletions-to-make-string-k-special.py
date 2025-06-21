class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # # DP- Memoization solution:
        # # char_map = defaultdict(int)
        # # for c in word:
        # #     char_map[c] += 1
        # # char_freq_arr = (list(char_map.values()))
        # # char_freq_arr.sort()
        
        # # # Dynamic Programming solution:
        # # dp = {}
        # # def dfs(arr):
        # #     if not arr or arr[-1] - arr[0] <= k:
        # #         return 0
            
        # #     if arr in dp:
        # #         return dp[arr]
            
        # #     res = float('inf')
        # #     # Decrease leftmost element or remove it
        # #     left_deletion = ((arr[0] - 1,) + arr[1:]) if arr[0] > 1 else arr[1:]
        # #     left_deletion = tuple(sorted(left_deletion))

        # #     right_deletion = (arr[:-1] + (arr[-1] - 1,)) if arr[-1] > 1 else arr[:-1]
        # #     right_deletion = tuple(sorted(right_deletion))

        # #     res = min(res, 1 + dfs(left_deletion))
        # #     res = min(res, 1 + dfs(right_deletion))

        # #     dp[arr] = res
        # #     return res

        # # return dfs(tuple(char_freq_arr))

        # char_map = defaultdict(int)
        # for c in word:
        #     char_map[c] += 1
        # char_freq_arr = tuple(sorted(char_map.values()))

        # dp = {}

        # def insert_sorted(arr, val):
        #     # Insert val into sorted tuple arr and return new tuple
        #     arr = list(arr)
        #     i = 0
        #     while i < len(arr) and arr[i] < val:
        #         i += 1
        #     return tuple(arr[:i] + [val] + arr[i:])

        # def dfs(arr):
        #     if not arr or arr[-1] - arr[0] <= k:
        #         return 0
        #     if arr in dp:
        #         return dp[arr]

        #     res = float('inf')

        #     # Decrease or remove leftmost element
        #     if arr[0] > 1:
        #         left_reduced = insert_sorted(arr[1:], arr[0] - 1)
        #     else:
        #         left_reduced = arr[1:]

        #     res = min(res, 1 + dfs(left_reduced))

        #     # Decrease or remove rightmost element
        #     if arr[-1] > 1:
        #         right_reduced = insert_sorted(arr[:-1], arr[-1] - 1)
        #     else:
        #         right_reduced = arr[:-1]

        #     res = min(res, 1 + dfs(right_reduced))

        #     dp[arr] = res
        #     return res

        # return dfs(char_freq_arr)


        # while l <= r and abs(char_freq_arr[l] - char_freq_arr[r]) > k:
        #     if char_freq_arr[l] == 1:
        #         if abs(char_freq_arr[l+1] - char_freq_arr[r]) < abs(char_freq_arr[l] - char_freq_arr[r])-1:
        #             l += 1
        #             deletions += 1
        #         else:
        #             char_freq_arr[r] -= 1
        #             deletions += 1
        #     else:
        #         if char_freq_arr[l] <= abs(char_freq_arr[l] - char_freq_arr[r]) - k:
        #             deletions += char_freq_arr[l]
        #             l += 1
        #         else:
        #             if abs(char_freq_arr[l]-1 - char_freq_arr[r]) < abs(char_freq_arr[l] - char_freq_arr[r]):
        #                 char_freq_arr[l] -= 1
        #                 deletions += 1
        #             else:
        #                 char_freq_arr[r] -= 1
        #                 deletions += 1

        # return deletions

        freq = sorted(Counter(word).values())
        n = len(freq)
        res = float('inf')

        for i in range(n):
            target = freq[i]
            deletions = sum(freq[j] for j in range(i))  # delete low-frequency characters
            for j in range(i+1, n):
                if freq[j] - target > k:
                    deletions += freq[j] - (target + k)
            res = min(res, deletions)

        return res

        
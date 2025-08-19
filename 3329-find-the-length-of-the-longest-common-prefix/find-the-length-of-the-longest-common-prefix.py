class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr_str_1 = [(str(num), 1) for num in arr1]
        arr_str_2 = [(str(num), 2) for num in arr2]
        combined = arr_str_1 + arr_str_2
        combined.sort(key=lambda x: x[0])

        lcp = 0

        def get_lcp(str1, str2):
            i, j = 0, 0
            lcp = 0
            while i < len(str1) and j < len(str2) and str1[i] == str2[j]:
                lcp += 1
                i += 1
                j += 1
            return lcp
        
        for i in range(len(combined)-1):
            str1, arr_1 = combined[i]
            str2, arr_2 = combined[i+1]
            if arr_1 != arr_2:
                lcp = max(lcp, get_lcp(str1, str2))
        
        return lcp
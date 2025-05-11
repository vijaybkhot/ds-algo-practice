class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        i, j, k = 0, 1, 2

        while k < len(arr):
            if arr[i] % 2 and arr[j] % 2 and arr[k] % 2:
                return True
            i += 1
            j += 1
            k += 1
        
        return False
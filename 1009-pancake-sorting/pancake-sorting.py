class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.res = []
        def flip(arr, k):
            arr_1 = arr[:k]
            arr_2 = arr[k:]
            self.res.append(k)
            return arr_1[::-1] + arr_2
        
        def max_idx(arr):
            max_idx = 0
            max_elem = arr[0]
            for i in range(len(arr)):
                if arr[i] > max_elem:
                    max_elem = arr[i]
                    max_idx = i
            return max_idx

        
        left, right = 0, len(arr)-1

        while left < right:
            max_i = left + max_idx(arr[left:right+1])
            arr = flip(arr, max_i+1)
            arr = flip(arr, right+1)
            right -= 1
        
        return self.res
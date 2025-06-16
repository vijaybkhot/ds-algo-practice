class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)

        left = 0
        count = 1
        while left+1 < len(arr) and arr[left] == arr[left+1]:
            left += 1
        if left+1 >= len(arr):
            return count
        left += 2
        res = 2
        count = 2

        while left < len(arr):
            
            if arr[left-2] > arr[left-1] < arr[left] or arr[left-2] < arr[left-1] > arr[left]:
                count += 1
                res = max(res, count)
            else:
                count = 2


            left += 1
        
        return res
        
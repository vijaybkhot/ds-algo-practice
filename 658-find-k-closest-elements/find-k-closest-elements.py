class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Using fixed length sliding window approach
        # Initializing a window
        left = 0
        for right in range(k, len(arr)):
            if abs(arr[right] - x) >= abs(arr[left] - x):
                continue
            else:
                # Remove left from window
                left = right-k+1
        
        return arr[left:left+k]
            

        
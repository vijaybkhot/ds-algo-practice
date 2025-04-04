class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # Get all elements in an array out of the grid
        arr = [col for row in grid for col in row]
        
        def isUnigridPossible(arr, x):
            sample_remainder = arr[0] % x
            for num in arr:
                if num % x != sample_remainder:
                    return False
            return True
        
        if not isUnigridPossible(arr, x):
            return -1
        
        def num_operations(target):
            operations = 0
            for num in arr:
                # Integer division instead of floating-point division
                operations += abs(target - num) // x
            return operations
        
        arr.sort()
        median = arr[len(arr) // 2]
        res = num_operations(median)
        
        return res
    
                
            
        
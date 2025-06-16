class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n

        # # Sliding Window approach
        # # Skip initial equal elements since they can't start a turbulent sequence
        # left = 0
        # while left + 1 < n and arr[left] == arr[left + 1]:
        #     left += 1
        
        # if left + 1 >= n:
        #     return 1  # All elements are equal

        # # Initialize count and result
        # count = 2  # Starting with a valid pair
        # max_len = 2
        # left += 2  # Start from the third element

        # while left < n:
        #     a, b, c = arr[left - 2], arr[left - 1], arr[left]

        #     # Check for turbulent pattern: > < or < >
        #     if (a > b < c) or (a < b > c):
        #         count += 1
        #         max_len = max(max_len, count)
        #     else:
        #         # If not turbulent, reset count to 2 (current and previous element)
        #         count = 2

        #     left += 1

        # return max_len

        # Using a signs array:
        signs = []
        for i in range(1,  len(arr)):
            if arr[i-1] > arr[i]:
                signs.append('>')
            elif arr[i-1] < arr[i]:
                signs.append('<')
            else:
                signs.append('=')

        
        res = 1 if signs[0] != '=' else 0
        curr_count = 1 if signs[0] != '=' else 0
        for i in range(1, len(signs)):
            if signs[i] != signs[i-1]:
                if signs[i] != '=':
                    curr_count += 1
                    res = max(curr_count, res)
                else:
                    curr_count = 0
            else:
                if signs[i] != '=':
                    curr_count = 1
                else:
                    curr_count = 0

        return res+1


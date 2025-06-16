class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n

        # Skip initial equal elements since they can't start a turbulent sequence
        left = 0
        while left + 1 < n and arr[left] == arr[left + 1]:
            left += 1
        
        if left + 1 >= n:
            return 1  # All elements are equal

        # Initialize count and result
        count = 2  # Starting with a valid pair
        max_len = 2
        left += 2  # Start from the third element

        while left < n:
            a, b, c = arr[left - 2], arr[left - 1], arr[left]

            # Check for turbulent pattern: > < or < >
            if (a > b < c) or (a < b > c):
                count += 1
                max_len = max(max_len, count)
            else:
                # If not turbulent, reset count to 2 (current and previous element)
                count = 2

            left += 1

        return max_len
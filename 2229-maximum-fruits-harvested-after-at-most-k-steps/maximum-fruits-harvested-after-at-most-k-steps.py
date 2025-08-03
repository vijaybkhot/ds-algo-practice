class Solution:
    def maxTotalFruits(
        self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        maxF = 0
        total = 0
        left = 0

        for right in range(n):
            total += fruits[right][1]

            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                left_first = abs(startPos - left_pos) + (right_pos - left_pos)
                right_first = abs(startPos - right_pos) + (right_pos - left_pos)

                if min(left_first, right_first) <= k:
                    break

                total -= fruits[left][1]
                left += 1
            
            maxF = max(maxF, total)
        
        return maxF
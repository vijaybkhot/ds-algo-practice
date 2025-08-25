from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        
        # build left prefix
        left_prefix = [0]
        for point in cardPoints:
            left_prefix.append(left_prefix[-1] + point)
        
        # build right prefix
        right_prefix = [0] * (n+1)
        for i in range(n-1, -1, -1):
            right_prefix[i] = right_prefix[i+1] + cardPoints[i]
        
        max_score = 0
        # try taking i from left, k-i from right
        for i in range(k+1):
            left_score = left_prefix[i]
            right_score = right_prefix[n-(k-i)]
            max_score = max(max_score, left_score + right_score)
        
        return max_score

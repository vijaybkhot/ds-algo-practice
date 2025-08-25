class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        # @lru_cache(None)
        # def dfs(left, right, curr_cards):
        #     if curr_cards == k:
        #         return 0
        #     if left > right:
        #         return float('-inf')
            
        #     # take left
        #     max_score = cardPoints[left] + dfs(left+1, right, curr_cards+1)
        #     # take right
        #     max_score = max(max_score, cardPoints[right] + dfs(left, right-1, curr_cards+1))

        #     return max_score
        
        # return dfs(0, len(cardPoints)-1, 0)
        
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
        print(left_prefix)
        print(right_prefix)
        for i in range(k+1):
            left_score = left_prefix[i]
            right_score = right_prefix[n-(k-i)]
            print(left_score+right_score)
            max_score = max(max_score, left_score+right_score)
        
        return max_score

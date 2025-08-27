class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        max_seq = 0

        # T F F T
        # F = 0


        #   Max Trues 
        F = 0
        for right, key in enumerate(answerKey):
            if key == 'F':
                F += 1
            while left <= right and F > k:
                if answerKey[left] == 'F':
                    F -= 1
                left += 1
            max_seq = max(max_seq, right - left + 1)
        
        #   Max False 
        T = 0
        left = 0
        for right, key in enumerate(answerKey):
            if key == 'T':
                T += 1
            while left <= right and T > k:
                if answerKey[left] == 'T':
                    T -= 1
                left += 1
            max_seq = max(max_seq, right - left + 1)
        
        return max_seq

            
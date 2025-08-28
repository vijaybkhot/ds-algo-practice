class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        counter = Counter()
        t_counter = Counter(t)
        curr_hold = 0
        min_len = len(s)
        min_str = ""

        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] == t_counter[s[right]]:
                curr_hold += 1

            while left <= right and  curr_hold >= len(t_counter):
                if right - left + 1 <= min_len:
                    min_len = right - left + 1
                    min_str = s[left:right+1]
                counter[s[left]] -= 1
                if counter[s[left]] < t_counter[s[left]]:
                    curr_hold -= 1
                left += 1
        
        return min_str
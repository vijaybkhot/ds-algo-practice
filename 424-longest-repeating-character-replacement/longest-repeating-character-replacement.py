class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq_map = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1 # Extend window
            max_freq = max(max_freq, freq_map[s[right]])

            while (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                if freq_map[s[left]] == max_freq:
                    max_freq = max(freq_map.values())
                left += 1 # Shrink window until a valid substring remains
            max_length = max(max_length, (right - left + 1))
        
        return max_length

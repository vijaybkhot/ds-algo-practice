class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {ch: 0 for ch in s}
        for ch in s:
            freq[ch] += 1
        
        stack = []
        
        in_stack = set()

        for char in s:
            freq[char] -= 1
            if char in in_stack:
                continue
            
            while stack and stack[-1] > char and freq[stack[-1]] > 0:
                popped_char = stack.pop()
                in_stack.remove(popped_char)
            
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)
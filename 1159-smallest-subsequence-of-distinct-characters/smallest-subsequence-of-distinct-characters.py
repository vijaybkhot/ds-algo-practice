class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        stack_set = set()
        in_stack = set()

        for char in s:
            counter[char] -= 1
            if char in in_stack:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                in_stack.remove(stack[-1])
                stack.pop()
            stack.append(char)
            in_stack.add(char)
            

            
            
        return ''.join(stack)
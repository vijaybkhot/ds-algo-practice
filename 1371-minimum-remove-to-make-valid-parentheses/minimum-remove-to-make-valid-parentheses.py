class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        paren_stack = []
        main_stack = []
        for idx, char in enumerate(s):
            if char == ")":
                if not paren_stack:
                    continue
                else:
                    paren_stack.pop()
            if char == "(":
                paren_stack.append(len(main_stack))
            main_stack.append(char)
        if paren_stack:
            for idx in paren_stack[::-1]:
                main_stack.pop(idx)
        return main_stack
        
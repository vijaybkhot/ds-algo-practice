class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)

        def get_num(idx):
            # Parse an integer starting at s[idx]
            curr_num = ""
            while idx < len(s) and s[idx] == ' ':
                idx += 1
            while idx < len(s) and s[idx].isdigit():
                curr_num += s[idx]
                idx += 1
            return int(curr_num), idx

        def calc_inside_paren(idx):
            stack = []
            sign = 1  # current sign
            num = 0

            while idx < n:
                ch = s[idx]

                if ch == ' ':
                    idx += 1
                    continue

                if ch.isdigit():
                    num, idx = get_num(idx)
                    stack.append(sign * num)

                elif ch == '+':
                    sign = 1
                    idx += 1

                elif ch == '-':
                    sign = -1
                    idx += 1

                elif ch == '(':
                    num, idx = calc_inside_paren(idx + 1)
                    stack.append(sign * num)

                elif ch == ')':
                    return sum(stack), idx + 1  # skip the closing ')'

                else:
                    idx += 1  # skip any other char (e.g. whitespace)

            return sum(stack), idx

        # Start from index 0 (outside parentheses)
        result, _ = calc_inside_paren(0)
        return result

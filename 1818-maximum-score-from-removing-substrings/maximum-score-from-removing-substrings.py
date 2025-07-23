class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # stack = [char for char in s]
        # score_map = {}
        # score_map['ab'] = x
        # score_map['ba'] = y
        # res = 0
        # def pop_target(target_pair, stack, gain):
        #     score = 0
        #     new_stack = []
        #     for i in range(len(stack)-1, -1, -1):
        #         new_stack.append(stack[i])
        #         while len(new_stack) > 1 and new_stack[-1]+new_stack[-2] == target_pair:
        #             new_stack.pop()
        #             new_stack.pop()
        #             score += gain
        #     return [new_stack[::-1], score]


        # if x >= y:
        #     stack_1, score1 = pop_target('ab', stack, x)
        #     stack_2, score2 = pop_target('ba', stack_1, y)
        # else:
        #     stack_1, score1 = pop_target('ba', stack, y)
        #     stack_2, score2 = pop_target('ab', stack_1, x)

        # return score1+score2
        # Readable solution:
        def remove_pair(s: str, a: str, b: str, gain: int) -> (str, int):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    score += gain
                else:
                    stack.append(ch)
            return "".join(stack), score

        if x >= y:
            # Remove "ab" first, then "ba"
            s, score1 = remove_pair(s, 'a', 'b', x)
            _, score2 = remove_pair(s, 'b', 'a', y)
        else:
            # Remove "ba" first, then "ab"
            s, score1 = remove_pair(s, 'b', 'a', y)
            _, score2 = remove_pair(s, 'a', 'b', x)

        return score1 + score2
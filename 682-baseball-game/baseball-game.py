class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        def is_valid_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        # Using stack to stack up and perform operations
        operation_stack = []
        for i in range(len(operations)-1, -1, -1):
            operation_stack.append(operations[i])
        
        res = []
        # Pop and perform each operation from the stack
        while operation_stack:
            curr_operation = operation_stack.pop()
            if is_valid_int(curr_operation):
                res.append(int(curr_operation))
            elif curr_operation == '+':
                res.append(res[-1] + res[-2])
            elif curr_operation == 'D':
                res.append(2 * res[-1])
            elif curr_operation == 'C':
                res.pop()
        
        return sum(res)
            
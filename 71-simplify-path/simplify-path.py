class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path_array = path.split('/')
        for path_str in path_array:
            if path_str == "" or path_str == ".":
                continue
            elif path_str == "..":
                if stack:
                    stack.pop()
                continue
            else:
                stack.append(path_str)
        return '/'+'/'.join(stack)
        
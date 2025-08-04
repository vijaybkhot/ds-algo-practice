class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_list = path.split("/")
        for name in path_list:
            if not name or name == ".":
                continue
            if name == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(name)
        
        res = ""

        for name in stack:
            res += '/' + name

        return "/" + res if not res else res

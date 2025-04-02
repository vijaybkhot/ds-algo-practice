# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     def inorder(node):
    #         inorder_str = ""
    #         if not node:
    #             return inorder_str
    #         stack = []
    #         curr = node
    #         while curr or stack:
    #             while curr:
    #                 stack.append(curr)
    #                 curr = curr.left
    #             curr = stack.pop()
    #             inorder_str += '#' + str(curr.val) + '#'
    #             curr = curr.right
    #         return inorder_str
        
    #     def preorder(node):
    #         preorder_str = ""
    #         if not node:
    #             return preorder_str
    #         stack = [node]
    #         while stack:
    #             curr = stack.pop()
    #             preorder_str += '#' + str(curr.val) + '#'
    #             if curr.right:
    #                 stack.append(curr.right)
    #             if curr.left:
    #                 stack.append(curr.left)
            
    #         return preorder_str
        
    #     preorder_str = preorder(root)
    #     inorder_str = inorder(root)
    #     combined_str = preorder_str + '$' + inorder_str

    #     return combined_str
        

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     preorder_str, inorder_str = data.split('$')
    #     # Construct an array using serialized str
    #     def constructArrFromStr(num_str):
    #         num_arr = []
    #         i = 0
    #         while i < len(num_str):
    #             while num_str[i] == '#':
    #                 i += 1
    #             curr_num = ""
    #             while num_str[i] != '#':
    #                 curr_num += num_str[i]
    #                 i += 1
    #             float_num = float(curr_num)
    #             num_arr.append(int(float_num))
    #             i += 1
    #         return num_arr
        
    #     preorder_arr = constructArrFromStr(preorder_str)
    #     inorder_arr = constructArrFromStr(inorder_str)

    #     # Construct a map of inorder indices
    #     inorder_map = {}
    #     for idx, num in enumerate(inorder_arr):
    #         if num not in inorder_map:
    #             inorder_map[num] = deque([])
    #         inorder_map[num].append(idx)
        
    #     self.pre_idx = 0

    #     def buildTree(left, right):
    #         if left > right:
    #             return None
            
    #         root_val = preorder_arr[self.pre_idx]
    #         self.pre_idx += 1
    #         root = TreeNode(root_val)
    #         inorder_idx = inorder_map[root_val].popleft()
    #         root.left = buildTree(left, inorder_idx-1)
    #         root.right = buildTree(inorder_idx+1, right)
    #         return root
        
    #     return buildTree(0, len(preorder_arr)-1)


    # Approach II: Using BFS
    def serialize(self, root):
        """Encodes a tree to a single string using BFS."""
        if not root:
            return ""

        queue = deque([root])
        res = []

        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")  # Explicitly store missing children
        
        return ",".join(res)    
                

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()
            
            # Left child
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            # Right child
            if values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root

        

    
        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
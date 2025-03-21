class ListNode:
    def __init__(self, val=0, index=0):
        self.val = val
        self.index=index
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.index_map = {}
        self.head = ListNode(val=0, index=-1)
        self.tail = ListNode(val=0, index=-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    


    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index > self.size-1:
            return -1
        curr = self.head.next
        while curr.index != index:
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val=val)
        next_node = self.head.next
        self.head.next, new_node.prev = new_node, self.head
        new_node.next, next_node.prev = next_node, new_node
        curr = next_node
        while curr != self.tail:
            curr.index += 1
            curr = curr.next
        self.size += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        prev_node = self.tail.prev
        new_node = ListNode(val=val, index=prev_node.index+1)
        prev_node.next = self.tail.prev = new_node
        new_node.prev, new_node.next = prev_node, self.tail
        self.size += 1



    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index > self.size or index < 0:
            return
        curr = self.head.next
        while curr.index != index-1:
            curr = curr.next
        new_node = ListNode(val=val, index=index)
        next_node = curr.next
        curr.next = next_node.prev = new_node
        new_node.prev, new_node.next = curr, next_node
        curr = next_node
        while curr != self.tail:
            curr.index += 1
            curr = curr.next
        
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0:
            return
        
        curr = self.head.next
        while curr.index != index:
            curr = curr.next
        
        prev_node, next_node = curr.prev, curr.next
        prev_node.next, next_node.prev = next_node, prev_node
        curr = next_node
        while curr != self.tail:
            curr.index -= 1
            curr = curr.next
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
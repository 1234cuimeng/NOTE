class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None
    def get(self, index):
        if index >= self.size or index < 0:
            raise Exception("超出链表节点的范围")
        p = self.head
        for i in range(index):
            p = p.next
        return p
    
    def insert(self, index, data):
        if index > self.size or index < 0:
            raise Exception("超出链表节点的范围")
        node = Node(data)
        if self.size == 0:
            print("此链表为空链表")
        # 头部插入
        elif index == 0:
            index.next = self.head
        # 尾部插人
        elif index == self.size:
             self.last.next = node
             self.last = node
        # 中间插入
        else:
            prev_node = self.get(index - 1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1
        
    def remove(self,index, data):
        if index >= self.size or index < 0:
            raise Exception("超出链表节点范围")
        # 暂存被删除的节点，用于返回
        if index == 0:
            # 删除头结点
            remove_node = self.head
            self.head = remove_node.next
        elif index == self.size - 1:
            # 删除尾节点
            prve_node = self.get(index - 1)
            remove_node = prve_node.next
            prve_node.next = None
            self.last =prve_node
        else:
            # 删除中间节点
            prev_node = self.get(index - 1)
            next_node = prev_node.next.next
            remove_node = prev_node.next
            prev_node.next =next_node
            
        self.size -= 1
        return remove_node
    
    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next
        
    
            
    

# 插入元素 尾部插入，中间插入，超范围插入
# append() insert()
# 删除元素:删除下标对应元素，直接删除元素
# pop() remove()
# 以下是删除操作代码：
# 以下是插入操作的代码：

class MyArray:
    def __init__(self, capacity):
        self.array = [None * capacity]
        self.size = 0
        
    def insert_v2(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围！")
        # 如果实际元素达到数组容量上限，数组扩容
        if self.size > len(self.array):
            self.resize()
        # 从右向左循环，逐个元素向右移
        for i in range(self.size-1, 0):
            self.array[i + 1] = self.array[i]
        # 腾出的位置放入新元素
        self.array[index] = element
        self.size += 1
        
    def resize(self):
        array_new = [None] * len(self.array) * 2
        # 从就数组复制到新数组
        for i in range(self.array):
            array_new[i] = self.array[i]
            
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出数组实际元素范围！")
        # 从左到右，逐个元素向左挪动一位：
        for i in range(0, self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1
        
    def output(self):
        for i in range(self.size):
            print(self.array[i])
            
            
array = MyArray(4)
array.insert_v2(0, 11)
array.insert_v2(0, 12)
array.insert_v2(0, 13)
array.output()
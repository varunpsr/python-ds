class BinaryHeap:
    '''
    This is an implementation for Binary Heap(minimum)
    '''

    def __init__(self):
        self.heap = [0]
        self.current_size = 0

    def percolate_up(self, index):
        while index // 2 > 0:
            # change this to greater than for Maximum heap.
            if self.heap[index] < self.heap[index//2]:
                temp = self.heap[index]
                self.heap[index] = self.heap[index//2]
                self.heap[index//2] = temp
            index = index // 2

    def insert(self, value):
        self.heap.append(value)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def min_child(self, index):
        if index * 2+1 > self.current_size:
            return index*2
        if self.heap[index*2] < self.heap[index*2+1]:
            return index*2
        else:
            return index*2+1

    def percolate_down(self, index):
        while index * 2 <= self.current_size:
            min_child = self.min_child(index)
            if self.heap[index] > self.heap[min_child]:
                temp = self.heap[index]
                self.heap[index] = self.heap[min_child]
                self.heap[min_child] = temp
            index = min_child

    def delete_minimum(self):
        min_val = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size -= 1
        self.heap.pop()
        print(f"Heap before balancing: {self.heap}")
        self.percolate_down(1)
        return min_val


minheap = BinaryHeap()
minheap.insert(33)
minheap.insert(7)
minheap.insert(17)
minheap.insert(10)
minheap.insert(15)
minheap.insert(3)
minheap.insert(14)

print(minheap.heap)

minheap.delete_minimum()
print(minheap.heap)

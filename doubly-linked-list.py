class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        if self is not None:
            return str(self.value)
        else:
            return "None"

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        print(f"adding new node: {node}")
        if self.head is None:
            print(f"Adding head node: {node}")
            self.head = node
        else:
            current_node = self.head
            previous_node = None

            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            print(f"old tail node: {current_node}")
            current_node.next = node
            print(f"new tail node: {node}")
            node.previous = current_node

    def print_list(self):
        current_node = self.head
        while current_node.next is not None:
            print(f"(prev:{current_node.previous}) {current_node}", end=' -> ')
            current_node = current_node.next
        print(f"(prev:{current_node.previous}) {current_node}", end=' -> ')
        print('None')


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
dll = DoublyLinkedList()
dll.add_node(node_1)
dll.add_node(node_2)
dll.add_node(node_3)
dll.print_list()
"""
1 -> 2 -> 5 -> \0

class - value, next
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def print_list(self):
        current_node = self.head
        while current_node.next is not None:
            print(current_node.value, end=' -> ')
            current_node = current_node.next
        print(current_node.value, end = ' -> ')
        print('None')


ll = LinkedList()

node = Node(1)
node_2 = Node(2)
node_3 = Node(5)

ll.add_node(node)
ll.add_node(node_2)
ll.add_node(node_3)

ll.print_list()
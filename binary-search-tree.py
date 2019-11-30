class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        if self is not None:
            return f"{self.value}"
        else:
            return "None"


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add_node(self, node):
        print(f"Adding node: {node}\n")
        if self.root is None:
            self.root = node
            print(f"Added root node: {self.root}")
        else:
            current_node = self.root
            while True:
                if node.value < current_node.value:
                    if current_node.left is None:
                        current_node.left = node
                        print(f"Adding {node} to left of {current_node}")
                        break
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        print(f"Adding {node} to right of {current_node}")
                        break
                    current_node = current_node.right

    def print_preorder(self, node):
        if node is not None:
            print(node)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_postorder(self, node):
        if node is not None:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node)

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node)
            self.print_inorder(node.right)


root = Node(7)
two = Node(2)
five = Node(5)
nine = Node(9)
eleven = Node(11)
bst = BinarySearchTree()
bst.add_node(root)
bst.add_node(two)
bst.add_node(five)
bst.add_node(nine)
bst.add_node(eleven)
bst.print_preorder(bst.root)
bst.print_inorder(bst.root)
bst.print_postorder(bst.root)
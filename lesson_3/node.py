class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'[{self.data}] -> {self.next}'


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(4)
    node_1.next = node_2
    node_3 = Node(5)
    node_2.next = node_3
    node_4 = Node(45)
    node_3.next = node_4
    print(node_1)

import LL1

class Node(LL1.Node):
    def kthToLast(self, k):
        node = self
        i = 0
        while(node != None and i < k):
            node = node.next
            i += 1
        return node






# Testing Area

class Product:
    def __init__(self, name):
        self.name = name

if(__name__ == "__main__"):

    node0 = Node(0)
    node0.next = Node(1)
    node0.next.next = Node(0)

    node = node0.kthToLast(2)
    node.transverse()
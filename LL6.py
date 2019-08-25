import LL1

class Node(LL1.Node):
    def addlr(self, ll):
        val1 = 0
        val2 = 0
        node1 = self
        node2 = ll

        i = 0
        while(node1 != None):
            val1 = val1*10 + node1.value
            node1 = node1.next
            i += 1
        i = 0
        while(node2 != None):
            val2 = val2*10 + node2.value
            node2 = node2.next
            i += 1

        return val1 + val2



# Testing Area

class Product:
    def __init__(self, name):
        self.name = name

if(__name__ == "__main__"):
    node0 = Node(1)
    node0.next = Node(2)
    node0.next.next = Node(3)

    node1 = Node(8)
    node1.next = Node(7)

    val = node0.addlr(node1)
    print(f'val = {val}')
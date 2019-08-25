import LL1

class Node(LL1.Node):
    def rmvDup(self):
        node = self
        nodeinit = node
        seen = [node.value]
        while(node.next != None):
            if(node.next.value in seen):
                node.next = node.next.next
            else:
                seen.append(node.next.value)
            if(node.next != None):
                node = node.next
        self = nodeinit


# Testing Area

class Product:
    def __init__(self, name):
        self.name = name

if(__name__ == "__main__"):
    node0 = Node(0)
    node0.next = Node(1)
    node0.next.next = Node(0)

    node0.transverse()
    node0.rmvDup()
    node0.transverse()

    p = Product("shoes")
    node0 = Node(p)
    node0.next = Node(Product("sneakers"))
    node0.next.next = Node(p)

    node0.rmvDup()
    node0.transverse()
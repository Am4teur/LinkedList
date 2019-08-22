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
    ll = Node(0)
    ll.next = Node(1)
    ll.next.next = Node(0)

    ll.rmvDup()
    ll.transverse()
    ll.transverse()

    p = Product("shoes")
    ll = Node(p)
    ll.next = Node(Product("sneakers"))
    ll.next.next = Node(p)

    ll.rmvDup()
    ll.transverse()
    ll.transverse()

        
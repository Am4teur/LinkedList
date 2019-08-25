import LL1

class Node(LL1.Node):
    def delete(self, k):
        if(k<0):
            return None
        node = self
        nodeinit = node
        if(k==0):
            nodeinit = nodeinit.next
        else:
            i = 1
            while(node.next != None):
                if(i == k):
                    node.next = node.next.next
                    break
                i += 1
                node = node.next
        return nodeinit



# Testing Area

class Product:
    def __init__(self, name):
        self.name = name

if(__name__ == "__main__"):
    ll = Node(0)
    ll.next = Node(1)
    ll.next.next = Node(2)
    ll.next.next.next = Node(3)

    node1 = ll.delete(-1)
    node1.transverse()
    ll.transverse()
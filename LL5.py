import LL4

class Node(LL4.Node):
    def addrl(self, ll):
        val1 = 0
        val2 = 0
        node1 = self
        node2 = ll

        i = 0
        while(node1 != None):
            val1 += node1.value*10**i
            node1 = node1.next
            i += 1
        i = 0
        while(node2 != None):
            val2 += node2.value*10**i
            node2 = node2.next
            i += 1

        val = val1 + val2
        print(f'f val = {val}')

        nodeinit = Node(0)
        node = nodeinit
        while(val > 10):
            node.next = Node(val%10)
            val = val//10
            node = node.next
        node.next = Node(val%10)
        
        return nodeinit.delete(0)




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

    val = node0.addrl(node1)
    val.transverse()
import LL0

class Node(LL0.Node):
    def transverse(self):
        node = self
        while(node != None):
            print(f'value = {node.value}')
            node = node.next


# Testing Area

if(__name__ == "__main__"):
    ll = Node(0)
    ll.next = Node(1)
    ll.next.next = Node(2)

    ll.transverse()

    ll.transverse()
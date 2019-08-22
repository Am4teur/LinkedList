class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def transverse(self):
        node = self
        while(node != None):
            print(f'value = {node.value}')
            node = node.next


ll = LinkedList(0)
ll.next = LinkedList(1)
ll.next.next = LinkedList(2)

ll.transverse()
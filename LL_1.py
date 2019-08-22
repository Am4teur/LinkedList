class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def transverse(self):
        while(self != None):
            self = self.next

            
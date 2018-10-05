from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, val):
        n = Node(val)
        n.setNext(self.head)
        self.tail =  self.head
        self.head = n

    def size(self):
        n = self.head
        count = 0
        while not n == None:
            count+=1
            n = n.getNext()
        return count

    def search(self,item):
        n = self.head
        found = False
        while not n == None:
            if n.getData() == item:
                found = True
                break
            else:
                n = n.getNext()
        if found:
            return True
        else:
            return False

    def remove(self, item):
        curn = self.head
        prev = None
        removed = False

        while curn != None:
            if curn.getData() != item:
                prev = curn
                curn = curn.getNext()
            else:
                if curn == self.head:
                    self.head = curn.getNext()
                elif curn.getNext() == None:
                    prev.setNext(None)
                else:
                    prev.setNext(curn.getNext())
                    curn.setNext(None)
                removed = True
                return True

        if curn == None and removed == False:
            return False


    def display(self):
        curn = self.head
        while curn != None:
            print ("{}".format(curn.getData()))
            curn = curn.getNext()

    def append(self, val):
        curn = self.head
        newnode = Node(val)
        while curn.getNext() != None:
            curn = curn.getNext()
        curn.setNext(newnode)
        self.tail = newnode

    def fast_append(self,val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            lastnode = self.tail
            lastnode.setNext(newnode)
            self.tail = newnode


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print("Size is {}".format(mylist.size()))

mylist.append(1)
mylist.display()

mylist.fast_append(23)
print("After fast append:")
mylist.display()

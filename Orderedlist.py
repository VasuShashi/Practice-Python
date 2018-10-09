from node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        node = self.head
        found = self.search(val)
        print("{} is {}".format(val, found))
        prev = None

        if found == False:
            newnode = Node(val)
            if self.head == None:
                self.head = newnode
            else:
                while node != None:
                    if node.getData() < val:
                        if node.getNext() == None:
                            node.setNext(newnode)
                            break
                        else:
                            prev = node
                            node = node.getNext()
                    else:
                        if prev == None:
                            newnode.setNext(node)
                            self.head = newnode
                            break
                        else:
                            prev.setNext(newnode)
                            newnode.setNext(node)
                            break

    def search(self, val):
        n = self.head
        while n != None:
            if n.getData() == val:
                return True
            else:
                n = n.getNext()
        return False

    def size(self):
        n = self.head
        count = 0
        while n != None:
            count+=1
            n = n.getNext()
        return count

    def display(self):
        curn = self.head
        while curn != None:
            print ("{}".format(curn.getData()))
            curn = curn.getNext()

mylist = OrderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print("Size is {}".format(mylist.size()))
mylist.display()

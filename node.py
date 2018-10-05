class Node:

    def __init__(self, val):
        self.data = val
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def setNext(self, nextnode):
        self.next = nextnode

    def getNext(self):
        return self.next

if __name__ == '__main__':
    main()

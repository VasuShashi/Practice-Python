class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def deq(self):
        return self.items.pop()

    def isEmpty(self):
        return (len(self.items) == 0)

    def size(self):
        return (len(self.items))

if __name__ == '__main__':
    main()

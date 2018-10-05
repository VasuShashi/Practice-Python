from queue import Queue

def play(num):
    q = Queue()
    numkids = int(raw_input("Eneter the number of kids: "))
    for i in range(numkids):
        kidname = str(raw_input("Enter the kid's name: "))
        q.enqueue(kidname)

    while not q.size() == 1:
        for i in range(num):
            kid = q.deq()
            q.enqueue(kid)
        q.deq()

    return q.deq()

print(play(7))

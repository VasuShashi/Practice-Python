from deq import DQueue

def checkpali(string):
    dq = DQueue()
    revstr = ""
    i = 0

    for ch in string:
        dq.addFront(ch)

    for i in range(len(string)):
        revstr += dq.removeFront()

    if revstr == string:
        print "Its a plaindrome"
    else:
        print "Its not"

checkpali("radar")

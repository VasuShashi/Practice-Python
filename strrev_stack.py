from stack import Stack

s = Stack()
string = str(raw_input("Enter a string to reverse: "))
for i in range(len(string)):
    s.push(string[i])

stklen = s.size()
revstr=''
for i in range(stklen):
    revstr+=(s.pop())

print(revstr)

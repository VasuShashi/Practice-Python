from stack import Stack

precedence = { "+":2,
                "-":2,
                "*":3,
                "/":3,
                "(":1 }

def intopost(string):
    lst = []
    s = Stack()
    opstr = ""
    toklist = string.split()

    for token in toklist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            lst.append(token)
        else:
            if token == '(':
                s.push(token)
            elif token == ')':
                tok = s.pop()
                while tok != '(':
                    lst.append(tok)
                    tok = s.pop()
            else:
                while not s.isEmpty() and precedence[token] <= precedence[s.peek()]:
                        lst.append(s.pop())
                s.push(token)

    while not s.isEmpty():
        lst.append(s.pop())

    print("".join(lst))

intopost("A + B * C")
intopost("A * B + C * D")
intopost("A * ( B + C ) * D")

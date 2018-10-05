from stack import Stack

def parcheck(string):
    s = Stack()
    balanced = True
    i = 0

    while i < len(string) and balanced :
        if string[i] == '(':
            s.push(string[i])
        else:
            if s.isEmpty():
                balanced = False
                break
            else:
                s.pop()
        i += 1

    if s.isEmpty() and balanced == True:
        print("Its balanced")
    else:
        print("Not balanced")

def balparChecker(string):
    s = Stack()
    balanced = True
    i = 0

    while i < len(string) and balanced :
        if string[i] in '([{':
            print("Pushing {}".format(string[i]))
            s.push(string[i])
        else:
            if s.isEmpty():
                balanced = False
                break
            else:
                comp = s.pop()
                print("comparing {} and {}".format(comp, string[i]))
                if not (comp == '(' and string[i] == ')' or \
                   comp == '{' and string[i] == '}' or \
                   comp == '[' and string[i] == ']' ) :
                   balanced = False
                   break
        i += 1

    if s.isEmpty() and balanced == True:
        print("Its balanced braces")
    else:
        print("Not balanced braces")

balparChecker('{{([][])}()}')
balparChecker('[{()]')

parcheck('(())')
parcheck('(()(())')
parcheck('(()(()))')

from stack import Stack

def evaluate(string):
    s = Stack()
    tokens = string.split()

    for token in tokens:
        print(token)
        if token in '+-*/':
            val2 = int(s.pop())
            val1 = int(s.pop())
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '*':
                result = val1 * val2
            elif token == '/':
                result = val1 / val2
            print(result)
            s.push(result)
        else:
            s.push(token)

    return s.pop()

print(evaluate('7 8 + 3 2 + /'))

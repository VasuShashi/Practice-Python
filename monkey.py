import string
import random

match  = "methinks it is like a weasel"
def gen_str(chars=string.ascii_lowercase + " "):
    while True:
        strgen = ''.join(random.choice(chars) for _ in range(27))
        if matchstr(strgen):
            print("Done")
            break

def matchstr(strgen):
    print ("%s == %s " % (strgen, match))
    if strgen in match:
        return 1
    return 0


gen_str()

dict = {}
def charpresent(in_str):
    for ch in in_str:
        if not ch in dict:
            dict[ch] = 1
            continue
        return ch
    return None

in_str = raw_input("Enter the string: ")
print("Recurring character is {}".format(charpresent(in_str)))

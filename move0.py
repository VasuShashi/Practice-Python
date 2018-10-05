arr = []
def mov0(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0 :
            arr[count] = arr[i]
            count+=1
    while count < n-1:
        arr[count] = 0
        count+=1
    return

size = int(raw_input("Size of the array: "))
i=0
while i < size:
    n = input("Element {}: ".format(i))
    arr.append(int(n))
    i+=1

mov0(arr, size)
for i in range(size):
    print(str(arr[i]) + " ")

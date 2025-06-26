array = [64, 34, 25, 12, 22, 11, 90]
 
n = len(array)

for i in range(n):
    isSwaped = False
    for j in range(n-i-1):
        if array[j] > array[j + 1]:
            array[j], array[j+1] = array[j+1], array[j]
            isSwaped = True
    if not isSwaped:
        break
print(array)

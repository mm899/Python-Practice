def bubbleSort(list, currentPass=0, leftPointer=0, rightPointer=1):
    if currentPass < len(list):
        while rightPointer != len(list):
            if list[leftPointer] > list[rightPointer]:
                temporary = list[leftPointer]
                list[leftPointer] = list[rightPointer]
                list[rightPointer] = temporary
            else:
                leftPointer += 1
                rightPointer += 1
        bubbleSort(list, currentPass+1)

testList = [99, 5, 4, 3 , 2, 1, 5, 4, 3 , 2, 1, 5, 4, 3 , 2, 1, 5, 4, 3 , 2, 1, 10000]

bubbleSort(testList)
print(testList)
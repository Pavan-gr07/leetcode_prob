def printArrayElementsRecurcive(arr,index):
    if index == len(arr):
        return
    
    print(arr[index],end=" ")

    printArrayElementsRecurcive(arr,index+1)


printArrayElementsRecurcive([1,2,3,4,5],0)
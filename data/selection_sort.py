def selection_sort(mylist):
    for i in range(len(mylist) - 1):
        index_min = i
        for j in range(i + 1, len(mylist)):
            if mylist[j] < mylist[index_min]:
                index_min = j
        if i != index_min:
            temp = mylist[i]
            mylist[i] = mylist[index_min]
            mylist[index_min] = temp
    return mylist


print(selection_sort([4, 3, 2, 1, 0]))

def insertion_sort(list_a):
    index_length = range(1,len(list_a))
    for i in index_length:
        start = list_a[i]

        while list_a[i-1] > start and i>0:
            list_a[i], list_a[i-1]= list_a[i-1],list_a[i]
            i = i-1

    return list_a

print(insertion_sort([7,8,5,2564,8,2,0,47,3]))

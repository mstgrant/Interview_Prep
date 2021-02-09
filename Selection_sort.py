#Time Complexity O(n^2)
#Space Complextiy O(1)

def selection_sort(list_a):
    index_a = range(0,len(list_a)-1)

    for i in index_a:
        min_value = i

        for j in range(i+1,len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]


    return list_a


print(selection_sort([7,85,9,5,2,1,2,0,5,785]))

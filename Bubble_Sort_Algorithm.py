#Time complexity O(n^2)
#Space complexity O(n)

def bubble_sort(list_a):
    # getting the length of the list
    index_length = len(list_a) -1
    #Making this false so that we can break the while loop
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,index_length):
            #comparing item on the left to the right and seeing if the item on the right is greater than the item on the left
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


#test
print(bubble_sort([9,200,10,1,5,0]))

# https://en.wikipedia.org/wiki/Merge_sort

def merge(left, right):
    # create an empty list to hold the sorted elements
    sortedList = []
    
    # there is no point in comparing the lists to sort them if one of them is
    # empty
    while len(left) != 0 and len(right) != 0:
        # depending on which element is smaller, we append that to the end of
        # the list that holds the sorted elements, then we remove that element
        # from the list
        if left[0] < right[0]:
            sortedList.append(left[0])
            left = left[1:]
        else:
            sortedList.append(right[0])
            right = right[1:]
    
    # at this point, the remaining part of the list can just be thrown on the
    # end of the sorted list, as it should be in a sorted order
    if len(left) == 0:
        sortedList += right
    else:
        sortedList += left
    
    return sortedList
        

def sort(toSort):
    # no need to sort if the list is 0 or 1 elements
    if len(toSort) == 0 or len(toSort) == 1:
        return toSort
        
    # divide the list
    halfWay = len(toSort)/2
    
    # recursively sort the halves of the list
    left = sort(toSort[:halfWay])
    right = sort(toSort[halfWay:])
    
    # return the merged halves to either the sort that called it recursively,
    # or the function that called sort originally
    return merge(left, right)


if __name__ == "__main__":
    print "import and call sort() rather than running this script"
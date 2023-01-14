



def findsmallest(arr:"list")->int:
    """ find the smallest number in the data
    INPUT : arr
    OUTPUT: indext if the smallest number
    """
    smallest_number = arr[0]
    smallest_index = 0

    for i in range(0,len(arr)):

        if smallest_number > arr[i]:
            smallest_number = arr[i]
            smallest_index = i
        else:
            pass

    return smallest_index





def findlargest(arr:"list")->int:

    """ find the largest number in the data
    INPUT : arr
    OUTPUT: indext if the largest number
    """

    largest_number = arr[0]
    largest_index = 0

    for i in range(0,len(arr)):

        if largest_number < arr[i]:
            largest_number = arr[i]
            largest_index = i

        else:
            pass

    return largest_index





def SelectionSort(arr:"list",sorting_type ="ASC")->"list":
    """sort the passed data either ASC(Ascending) or DESC(Descending)

    INPUT : arr data you need to sort
            sorting_type either ASC or DESC , if user did not write the type it's by default ASC
    OUTPUT: sorted list
    """
    newarr = []
    sorting_type = sorting_type.upper()

    if sorting_type != "ASC" and sorting_type != "DECS" :
        print("*"*100)
        print("Wrong sorting type input , so the algorithm used the default sorting_typetype ASC")
        print("*"*100)

    else:
        pass


    for i in range(0,len(arr)):
        if sorting_type == "asc" or sorting_type == "ASC":
            newarr.append(arr.pop(findsmallest(arr)))

        elif sorting_type == "asc" or sorting_type == "DESC":
            newarr.append(arr.pop(findlargest(arr)))

        else:
            newarr.append(arr.pop(findsmallest(arr)))


    return newarr






# Example
if __name__ == "__main__":

    data = [1,8,2,6,985,6,2,6,95,21,1,23562,100]

    data = SelectionSort(data)
    print(data)

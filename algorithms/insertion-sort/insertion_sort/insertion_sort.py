


def insertion_sort(arr):
    """ 
    Insertion sort algorithm function takes in an array of integers as an argument:
    1. Start at the first element in the array
    2. Compare the current element with the element before it
    3. If the current element is smaller than the element before it, swap them
    4. Repeat until the array is sorted


    """
    try:
        for i in range(1,len(arr)):
            # raise error if the array elements are not integers
            j = i-1
            # temp min value of the array
            temp = arr[i]
            # while the temp value is less than the value at the jth index
            while temp < arr[j] and j >= 0:
                # swap the values
                arr[j+1] = arr[j]
                j -= 1
            # insert the temp value into the jth index
            arr[j+1] = temp  
    except Exception:
        return 'Array elements must be integers'

    return arr

# def reverse_sorted(arr):
#     """
#     Reverse sorted algorithm function takes in an array of integers as an argument:
#     1. Start at the last element in the array
#     2. Compare the current element with the element before it
#     3. If the current element is greater than the element before it, swap them
#     4. Repeat until the array is sorted

#     """
#     for i in range(1,len(arr)):
#         j = i - 1
#         temp = arr[i]
#         while j >=0 and temp > arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = temp

#     return arr




if __name__ == "__main__":    
    print(insertion_sort([2,3,5,20,1,-1]))
    print(reverse_sorted([2,3,5,20,1,-1]))
    print(insertion_sort([]))





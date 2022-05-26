def merge_sort(arr):
    """
    Merge sort algorithm that takes array as an argument and returns a sorted array.
    """
    array_length = len(arr)
    if array_length > 1:
        mid = array_length // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
    return arr
        
def merge(left,right,arr):
    """
    merge function takes 3 arguments: left, right, array.
    left and right are the left and right halves of the array.
    arr is the array that is being sorted.

    """
    try:
        left_index = 0
        right_index = 0
        array_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                arr[array_index] = left[left_index]
                left_index += 1
            else:
                arr[array_index] = right[right_index]
                right_index += 1
            array_index += 1
        while left_index < len(left):
            arr[array_index] = left[left_index]
            left_index += 1
            array_index += 1
        while right_index < len(right):
            arr[array_index] = right[right_index]
            right_index += 1
            array_index += 1
    except Exception:
        raise Exception("Array elements must be integers")

if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    merge_sort(arr)
    print(arr)



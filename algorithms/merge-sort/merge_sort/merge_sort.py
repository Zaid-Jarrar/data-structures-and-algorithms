"""
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
"""

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



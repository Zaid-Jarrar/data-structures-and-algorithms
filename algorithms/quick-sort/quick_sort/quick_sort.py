def quicksort(arr):
    if type(arr) != list:
        raise TypeError("Input must be a list")
    return quick_sort(arr,0,len(arr)-1)

def quick_sort(arr,left,right):
    if left < right:
        pivot = partition(arr,left,right)
        quick_sort(arr,left,pivot - 1)
        quick_sort(arr,pivot + 1, right)

def partition(arr,left,right):
    try:
        pivot = arr[right]
        low = left -1
        for index in range(left,right):
            if arr[index] <= pivot:
                low += 1
                swap(arr,index,low)
        swap(arr,right,low + 1)
        return low + 1
    except Exception :
        raise Exception("Input must be a list of integers")

def swap(arr,index,low):
    temp = arr[index]
    arr[index] = arr[low]
    arr[low] = temp

if __name__ == '__main__':
    arr = [True,False]
    quicksort(arr)
    # quick_sort(arr,0,len(arr)-1)
    print(arr)

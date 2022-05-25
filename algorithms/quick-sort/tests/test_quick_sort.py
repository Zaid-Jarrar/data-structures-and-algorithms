from quick_sort.quick_sort import quick_sort


def test_quick_sort():
    arr = [5,4,3,2,1]
    quick_sort(arr,0,len(arr)-1)
    assert arr == [1,2,3,4,5]


def test_quick_sort_empty():
    arr = []
    quick_sort(arr,0,len(arr)-1)
    assert arr == []


def test_quick_sort_one():
    arr = [1]
    quick_sort(arr,0,len(arr)-1)
    assert arr == [1]

def test_quick_sort_two():
    arr = [1,2]
    quick_sort(arr,0,len(arr)-1)
    assert arr == [1,2]



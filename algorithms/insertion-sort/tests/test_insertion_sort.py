from insertion_sort.insertion_sort import insertion_sort


def test_insertion_sort():
    arr = [5, -1, 10, -5]
    actual = insertion_sort(arr)
    expected = [-5, -1, 5, 10]
    assert actual == expected

def test_insertion_sort2():
    arr = [8,4,23,42,16,15]
    actual = insertion_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_insertion_sort_fail():
   
    arr = [8,4,23,42,16,15, 'hello']
    actual = insertion_sort(arr)
    expected = 'Array elements must be integers'
    assert actual == expected

def test_insertion_sort3():
   
    arr = []
    actual = insertion_sort(arr)
    expected = []
    assert actual == expected

def test_insertion_sort4():
   
    arr = [1,-5]
    actual = insertion_sort(arr)
    expected = [-5,1]
    assert actual == expected
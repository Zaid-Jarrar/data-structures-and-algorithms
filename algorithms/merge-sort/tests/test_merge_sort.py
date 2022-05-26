from merge_sort.merge_sort import merge_sort
import pytest

def test_merge_sort():
    array = [12, 11, 13, 5, 6, 7 ]
    actual = merge_sort(array)
    expected = [5, 6, 7, 11, 12, 13]
    assert actual == expected

def test_merge_sort2():
    array = [12, 11, 13, 5, 6 ]
    actual = merge_sort(array)
    expected = [5, 6, 11, 12, 13]
    assert actual == expected

def test_merge_sort3():
    array = []
    actual = merge_sort(array)
    expected = []
    assert actual == expected   

def test_merge_sort4():
    array = [1]
    actual = merge_sort(array)
    expected = [1]
    assert actual == expected    

def test_merge_sort_exception():
    with pytest.raises(Exception):
        array = [12, 11, 13, 5, 6, '7' ]
        actual = merge_sort(array)



    

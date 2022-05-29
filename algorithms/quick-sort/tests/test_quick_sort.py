import pytest
from quick_sort.quick_sort import quicksort


def test_quick_sort():
    arr = [5,4,3,2,1]
    quicksort(arr)
    expected=[1,2,3,4,5]
    assert arr == expected


def test_quick_sort_empty():
    arr = []
    quicksort(arr)
    expected=[]
    assert arr == expected



def test_quick_sort_one():
    arr = [1]
    quicksort(arr)
    expected=[1]
    assert arr == expected


def test_quick_sort_two():
    arr = [2,1]
    quicksort(arr)
    expected=[1,2]
    assert arr == expected

def test_quick_sort_fails():
    with pytest.raises(Exception):
        quicksort(1)

def test_quick_sort_string():
    arr = ['5','4','3','2','1']
    quicksort(arr)
    assert arr == ['1','2','3','4','5']


def test_quick_sort_boolean():
    arr = [True,False]
    quicksort(arr)
    assert arr == [False,True]
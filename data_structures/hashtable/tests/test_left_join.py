import pytest
from hashtable.hashtable_leftjoin import HashTable, left_join


def test_left_join():
    ht1 = HashTable()
    ht1.set('fond', 'enamored')
    ht1.set('wrath', 'anger')
    ht1.set('diligent', 'employed')
    ht1.set('outfit', 'garb')
    ht1.set('guide', 'usher')

    ht2 = HashTable()
    ht2.set('fond', 'averse')
    ht2.set('wrath', 'delight')
    ht2.set('diligent', 'idle') 
    ht2.set('guide', 'follow')

    ht3 = left_join(ht1, ht2)
    assert ht3.get('wrath') == ['anger', 'delight']
    assert ht3.get('fond') == ['enamored', 'averse']
    assert ht3.get('diligent') == ['employed', 'idle']
    assert ht3.get('guide') == ['usher', 'follow']
    assert ht3.get('outfit') == ['garb', 'Null']


def test_left_join_error():
    with pytest.raises(Exception):
        ht1 = HashTable()
        ht1.set('fond', 'enamored')

        ht2 = []
        ht2.append(1)
        left_join(ht1, ht2)

def test_left_join_error2():
    with pytest.raises(Exception):
        ht1 = HashTable()
        ht1.set(1, 'enamored')

        ht2 = HashTable()
        ht2.set('fond', 'averse')
        left_join(ht1, ht2)



def test_left_join_collsion():
    ht1 = HashTable()
    ht1.set('fond', 'enamored')
    ht1.set('ofnd','collosion')
    ht1.set('wrath', 'anger')
    ht1.set('diligent', 'employed')
    ht1.set('outfit', 'garb')
    ht1.set('guide', 'usher')

    ht2 = HashTable()
    ht2.set('fond', 'averse')
    ht2.set('wrath', 'delight')
    ht2.set('diligent', 'idle') 
    ht2.set('guide', 'follow')

    ht3 = left_join(ht1, ht2)
    assert ht3.get('fond') == ['enamored', 'averse']
    assert ht3.get('ofnd') == ['collosion', 'Null']


def test_left_join_empty():
    ht1 = HashTable()
    ht1.set('fond', 'enamored')
    ht2= HashTable()
    ht3 = left_join(ht1, ht2)
    assert ht3.get('fond') == ['enamored', 'Null']


def test_left_join_empty_both():

    ht1 = HashTable()
    ht2 = HashTable()
    ht3=left_join(ht1, ht2)

    assert ht3.keys() == []








import pytest
from hashtable.hashtable import HashTable


def test_hash_set():
    hash = HashTable()
    hash.set("phone", "G20")

    actual= hash.get('phone')
    expected = "G20"
    assert actual == expected
    

def test_hash_get():
    hash = HashTable()
    hash.set("phone", "G20")

    actual= hash.get('phone')
    expected = "G20"
    assert actual == expected


def test_hash_get_null():
    hash = HashTable()

    actual= hash.get('phone')
    expected = None
    assert actual == expected

def test_hash_keys():
    hash = HashTable()
    hash.set("phone", "G20")
    hash.set("name", "google")
    hash.set("device", "keyboard")
    actual= hash.keys()
    expected = [ "device", "name","phone",]
    assert actual == expected

def test_hash_collision():
    hash = HashTable()
    hash.set("cat", "meow")
    hash.set("act", "homework")

    actual= hash.get("cat")
    expected = "meow"
    assert actual == expected

def test_hash_hashkey():
    hash = HashTable()
    hash.set("cat", "meow")
    actual= hash.hash("cat")
    expected = 808
    assert actual == expected

def test_hash_fail():
    with pytest.raises(Exception):
        hash = HashTable()
        hash.set(1, "meow")   

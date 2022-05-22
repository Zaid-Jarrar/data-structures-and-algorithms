import pytest
from hashtable.hashtable_ import HashTable
from hashtable.hashtable_repeated_word import repeated_word



# --------------------------hashmap_repeated_word tests-------------------#
def test_repeated_word():
    text = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(text)
    expected = "a"
    assert actual == expected

def test_repeated_word2():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(text)
    expected = "it"
    assert actual == expected


def test_repeated_word3():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = repeated_word(text)
    expected = "summer"
    assert actual == expected

def test_repeated_word_fail():
    with pytest.raises(Exception):
        text = 12
        repeated_word(12)

#--------------------HashTable tests-------------------#
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
    assert hash.table[808] == [{'cat': 'meow'}, {'act': 'homework'}]
    assert hash.get("cat") == "meow"
    assert hash.get("act") == "homework"

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

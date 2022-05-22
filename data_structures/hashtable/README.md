# Hashtables
<!-- Short summary or background information -->
Hashtables are data structures that store data in key-value pairs.
and if a collison happens within the table then it would be added to the same index without overwriting the previous value.

## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:
set(key, value)
get(key)
contains(key)
keys()
hash(key)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O is (n) because of the possibility of collision.
but wit a perfect hash table it would be a O(1)


## API
<!-- Description of each method publicly available in each of your hashtable -->
    """
    HashTable is a class that inherits from object and has the following methods:

    hash(self,key): hash function that takes a key and returns an index in the hashtable. Time complixity is O(n) and space complexity is O(1)

    set(self,key,value): sets a key and value in the hashtable, O(n) space complexity and O(1) time complexity if key index doesnt exist and O(n) time and space complexity is O(n) if key index does exist.

    get(self,key): gets the value of a key, O(n) time complexity and O(1) space complexity

    contains(self,key): checks if a key is in the hashtable, O(n) time complexity and O(1) space complexity

    keys(self): returns a list of all keys in the hashtable, O(n^3) time complexity and O(n) space complexity
    """
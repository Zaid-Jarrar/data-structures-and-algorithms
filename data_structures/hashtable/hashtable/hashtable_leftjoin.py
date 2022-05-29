class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * size
        # self.table = [LinkedList()]*size

    def hash(self, key):
        """
        A method to hash the key according to ASCII size
        Input: key
        Output: hash value
        """
        if type(key) is not str:
            raise Exception("Key must be a string")
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)  # 86
            sum_of_ascii += ch_ascii
        hashed_key = (sum_of_ascii * 19) % self.size
        return hashed_key

    def set(self, key, value):
        """
        A method to hash the key, then set the key and value pair in the table, handling collisions as needed
        Input: key, value
        Output: othing
        """
        if type(key) is not str and type(value) is not str:
            raise Exception("Key and Value must be strings")
        idx = self.hash(key)
        if not self.table[idx]:
            self.table[idx] = [[key, value]]  # LinkedList().add({key, value})
        else:
            self.table[idx].append([key, value])

    def get(self, key):
        """
        A method to retrieve the value of a key
        Input: key
        Output: value
        """
        if type(key) is not str:
            raise Exception("Key must be a string")
        index = self.hash(key)
        if not self.table[index]:
            return None
        for arr in self.table[index]:
            if arr[0] == key:
                return arr[1]

    def keys(self):
        """
        A method to retrieve the keys of a hash table
        Input: nothing
        Output: list of keys
        """       
        keys = []
        for bucket in self.table:
            if bucket is not None:
                for arr in bucket:
                    keys.append(arr[0])
        return keys



    def contains(self, key):
        """
        A method to check if the key is already in the hash table
        Input: key
        Output: boolean
        """
        if type(key) is not str:
            raise Exception("Key must be a string")
        if self.get(key):
            return True
        else:
            return False

    def __str__(self):
        output = ""
        for bucket in self.table:
            if bucket is not None:
                output += f"{bucket} \n"
        return output


def left_join(ht1, ht2):

    """
    A function used to join two hash tables into a new hash table
    with the keys from ht1 and the values from ht1 and ht2 values
    Input: ht1, ht2
    Output: ht3
    """
    if type(ht1) is not HashTable or type(ht2) is not HashTable:
        raise Exception("Both hash tables must be HashTable objects")    

    ht3 = HashTable()

    for key in ht1.keys():        
        if ht2.contains(key):
            ht3.set(key, [ht1.get(key), ht2.get(key)])
        else:
            ht3.set(key, [ht1.get(key), 'Null'])
        
    return ht3


if __name__ == "__main__":
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


    print(ht3)
    # print(ht2)
    # print(ht1)



    # ht1 = HashTable()
    # ht1.set('fond', 'enamored')
    # ht1.set('ofnd','enamored22')
    # ht1.set('wrath', 'anger')
    # ht1.set('diligent', 'employed')
    # ht1.set('outfit', 'garb')
    # ht1.set('guide', 'usher')

    # ht2 = HashTable()
    # ht2.set('fond', 'averse')
    # ht2.set('wrath', 'delight')
    # ht2.set('diligent', 'idle') 
    # ht2.set('guide', 'follow')

    # ht3 = left_join(ht1, ht2)
    # print(ht3)

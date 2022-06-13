class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        # adding the __ before the table made it not accessible outside of the class
        self.__table = [None] * size
        # self.__table = [LinkedList()]*size

    def hash(self, key):
        """
        A method to hash the key according to ASCII size
        Input: key
        Output: hash value
        """
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)  # 86
            sum_of_ascii += ch_ascii
        hashed_key = (sum_of_ascii * 19) % self.size
        return hashed_key

    def set(self, key, value):
        """
        A method to hash the key, then set the key and value pair in the __table, handling collisions as needed
        Input: key, value
        Output: othing
        """
        idx = self.hash(key)
        if not self.__table[idx]:
            self.__table[idx] = [[key, value]]  # LinkedList().add({key, value})
        else:
            self.__table[idx].append([key, value])

    def get(self, key):
        """
        A method to retrieve the vlaue of a key
        Input: key
        Output: value
        """
        return self.__table[self.hash(key)]

    def keys(self):
        """
        A method to retrieve the keys of a hash __table
        Input: nothing
        Output: list of keys
        """
        # return [key[0][0] for key in self.__table if key is not None]
        keys = []
        for bucket in self.__table:
            if bucket is not None:
                keys.append(bucket[0][0])
        return keys



    def contains(self, key):
        """
        A method to check if the key is already in the hash __table
        Input: key
        Output: boolean
        """
        if self.get(key) is not None:
            return True
        else:
            return False

    def __str__(self):
        output = ""
        for bucket in self.__table:
            if bucket is not None:
                output += f"{bucket} \n"
        return output


if __name__ == '__main__':
    # pass
    hashtable = HashTable()
    hashtable.set("a", 1)
    hashtable.set("b", 2)
    print(hashtable.get("a"))
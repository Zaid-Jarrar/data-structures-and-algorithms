class HashTable(object):
    """
    HashTable is a class that inherits from object and has the following methods:

    hash(self,key): hash function that takes a key and returns an index in the hashtable
    set(self,key,value): sets a key and value in the hashtable
    get(self,key): gets the value of a key
    contains(self,key): checks if a key is in the hashtable
    keys(self): returns a list of all keys in the hashtable
    """
    def __init__(self,size = 1024):
        self.size = size
        self.table = [None] * size

    def hash(self,key):
        if type(key) is not str:
            raise Exception("Key must be a string")
        sum_ascii_value = 0
        for char in key:
            char_value =  ord(char)
            sum_ascii_value += char_value
        sum_ascii_value = (sum_ascii_value*19) % self.size
        return sum_ascii_value

    def set(self,key,value):
        if type(key) is not str and type(value) is not str:
                raise Exception("Key and Value must be strings")
        index = self.hash(key)
        if not self.table[index]:
            self.table[index] = [{f"{key}":f"{value}"}]

        elif self.table[index]:
            if key in self.keys():
                for dic in self.table[index]:
                    if key in dic.keys():
                        dic[key] = value
            else:
                self.table[index].append({f"{key}":f"{value}"})
                            
    def get(self,key):
        if type(key) is not str:
            raise Exception("Key must be a string")
        index = self.hash(key)
        if not self.table[index]:
            return None
        for dic in self.table[index]:
            if key in dic.keys():
                return dic[key]
   
    def contains(self,key):
        if type(key) is not str:
            raise Exception("Key must be a string")
        index = self.hash(key)
        if not self.table[index]:
            return False
        for dic in self.table[index]:
            if key in dic.keys():
                return True
            return False
     
    def keys(self):
        keys = []
        for index in self.table:
            if index:
                for dic in index:
                    for key in dic.keys():
                        keys.append(key)
                        
        return keys


if __name__ == '__main__':
    hash = HashTable()
    hash.set('cat','meow')
    hash.set('Dog','woof')
    hash.set('cat','dog')
    hash.set('ogD','why')
    print(hash.keys())

    hash.set('ogD','new')
    # print(hash.get('cat'))
    print(hash.contains('atc'))

    # print(hash.table[238])
    for i in enumerate(hash.table):
        print(i)



# class HashTable(object):
#     def __init__(self, size=1024):
#         self.size = size
#         self.table = [None] * size
#         # self.table = [LinkedList()]*size

#     def hash(self, key):
#         """
#         A method to hash the key according to ASCII size
#         Input: key
#         Output: hash value
#         """
#         sum_of_ascii = 0
#         for ch in key:
#             ch_ascii = ord(ch)  # 86
#             sum_of_ascii += ch_ascii
#         hashed_key = (sum_of_ascii * 19) % self.size
#         return hashed_key

#     def set(self, key, value):
#         """
#         A method to hash the key, then set the key and value pair in the table, handling collisions as needed
#         Input: key, value
#         Output: othing
#         """
#         idx = self.hash(key)
#         if not self.table[idx]:
#             self.table[idx] = [[key, value]]  # LinkedList().add({key, value})
#         else:
#             self.table[idx].append([key, value])

#     def get(self, key):
#         """
#         A method to retrieve the vlaue of a key
#         Input: key
#         Output: value
#         """
#         return self.table[self.hash(key)]

#     def keys(self):
#         """
#         A method to retrieve the keys of a hash table
#         Input: nothing
#         Output: list of keys
#         """
#         # return [key[0][0] for key in self.table if key is not None]
#         keys = []
#         for bucket in self.table:
#             if bucket is not None:
#                 keys.append(bucket[0][0])
#         return keys



#     def contains(self, key):
#         """
#         A method to check if the key is already in the hash table
#         Input: key
#         Output: boolean
#         """
#         if self.get(key) is not None:
#             return True
#         else:
#             return False

#     def __str__(self):
#         output = ""
#         for bucket in self.table:
#             if bucket is not None:
#                 output += f"{bucket} \n"
#         return output
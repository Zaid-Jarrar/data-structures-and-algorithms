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

    print(hash.table[238])
    # for i in enumerate(hash.table[238]):
    #     print(i)



    # print(hash.table[238])
    # dict = [{'dog':"woof"}, {"ogD":"meow"}]
    # for dic in dict:
    #     if 'dog' in dic.keys():
    #         dic['dog'] = 'yes'
    #     print(dic)
            # print('yes')
        # print(dic.keys())
        # print(dic['dog'])
    # def set(self,key,value):
    #     index = self.hash(key)
    #     if not self.table[index]:
    #         self.table[index] = {f"{key}": f"{value}"}
    #     else:
    #         self.table[index][key] = value

    # def get(self,key):
    #     index = self.hash(key)
    #     return self.table[index][key]


    # def contains(self,key):
    #     index = self.hash(key)
    #     if not self.table[index]:
    #         return False    
    #     if key in hash.table[index]:
    #         return True
    #     return False
     
    # def keys(self):
    #     keys_collection = []
    #     for index in self.table:
    #         if index:
    #             keys_collection += index.keys()
    #     return keys_collection

    # print(hash.hash('Cat'))
    # print(hash.hash('aCt'))

    # hash.set('Cat', 'meow')
    # hash.set('aCt', 'wolf')
    # # hash.set('aCt', 'dog')


    # # for i in enumerate(hash.table):
    # #     print(i)
    # print(hash.get('Cat'))
    # # print(hash.get('aCt'))


    # print(hash.table[200])
    # print(hash.contains('aCtt'))
    # # a= hash.table[200].keys()
    # # print(list(a))
    # print(hash.keys())